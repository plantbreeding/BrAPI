#!/usr/bin/env python3
"""
Check and fix nullable consistency between YAML NewRequest schemas and JSON entity schemas.

For each *NewRequest.yaml, any property marked nullable: true must also be nullable
in the corresponding *.json entity schema in BrAPI-Schema.

Usage:
    python checkNullableConsistency.py [--fix] [--root <workspace_root>]

Options:
    --fix   Apply fixes to JSON files (default: dry run / report only)
    --root  Root of the BrAPI workspace (default: current directory)
"""

import yaml
import json
import glob
import os
import sys
import copy


def find_json_entity_file(entity_name, schema_root):
    """Find the JSON schema file for an entity name in BrAPI-Schema."""
    matches = glob.glob(os.path.join(schema_root, "**", f"{entity_name}.json"), recursive=True)
    # Exclude files in Requests/ subfolder
    matches = [m for m in matches if "Requests" not in m.replace("\\", "/")]
    return matches[0] if matches else None


def collect_nullable_yaml_properties(schema_def, prefix=""):
    """
    Recursively collect all property names (top-level only) that are nullable: true
    from an OpenAPI schema definition. Returns dict of {prop_name: prop_def}.
    """
    nullable = {}
    for prop_name, prop_def in schema_def.get("properties", {}).items():
        if prop_def.get("nullable", False):
            nullable[prefix + prop_name] = prop_def
    return nullable


def derive_json_rel_name(yaml_prop_name):
    """
    Given a YAML flat property name like 'programDbId' or 'programName',
    derive the likely JSON relationship field name (e.g. 'program').
    Returns the candidate name, or None if the pattern doesn't apply.
    """
    for suffix in ("DbId", "Name", "PUI"):
        if yaml_prop_name.endswith(suffix) and len(yaml_prop_name) > len(suffix):
            return yaml_prop_name[: -len(suffix)]
    return None


def is_nullable_in_json(json_prop):
    """Return True if a JSON Schema property is already nullable."""
    prop_type = json_prop.get("type", "")
    if isinstance(prop_type, list) and "null" in prop_type:
        return True
    if "anyOf" in json_prop:
        for item in json_prop["anyOf"]:
            if item.get("type") == "null":
                return True
    return False


def make_nullable_in_json(json_prop):
    """
    Return a copy of json_prop that is nullable.
    - If the property has a $ref (and no anyOf yet), wrap $ref in anyOf with null.
    - If the property has a simple type, change to ["null", type].
    """
    prop = copy.deepcopy(json_prop)

    if "$ref" in prop:
        ref = prop.pop("$ref")
        anyof_entry = {"$ref": ref}
        prop["anyOf"] = [anyof_entry, {"type": "null"}]
        return prop

    prop_type = prop.get("type")
    if isinstance(prop_type, str):
        prop["type"] = ["null", prop_type]
    elif isinstance(prop_type, list) and "null" not in prop_type:
        prop["type"] = ["null"] + prop_type

    # Also ensure null is in enum if present
    if "enum" in prop and None not in prop["enum"]:
        prop["enum"] = prop["enum"] + [None]

    return prop


def get_entity_name_from_yaml(yaml_path):
    """Derive entity name from a *NewRequest.yaml path."""
    basename = os.path.basename(yaml_path)
    return basename.replace("NewRequest.yaml", "")


def main():
    fix_mode = "--fix" in sys.argv
    root = "."
    if "--root" in sys.argv:
        idx = sys.argv.index("--root")
        root = sys.argv[idx + 1]

    yaml_root = os.path.join(root, "Specification")
    schema_root = os.path.join(root, "Specification", "BrAPI-Schema")

    yaml_files = sorted(glob.glob(
        os.path.join(yaml_root, "**", "*NewRequest.yaml"), recursive=True
    ))

    total_issues = 0
    total_fixed = 0

    for yaml_file in yaml_files:
        entity_name = get_entity_name_from_yaml(yaml_file)

        json_file = find_json_entity_file(entity_name, schema_root)
        if not json_file:
            print(f"[SKIP] No JSON file found for '{entity_name}' (from {os.path.basename(yaml_file)})")
            continue

        with open(yaml_file, "r", encoding="utf-8") as f:
            try:
                yaml_obj = yaml.safe_load(f)
            except yaml.YAMLError as e:
                print(f"[ERROR] Failed to parse {yaml_file}: {e}")
                continue

        with open(json_file, "r", encoding="utf-8") as f:
            try:
                json_obj = json.load(f)
            except json.JSONDecodeError as e:
                print(f"[ERROR] Failed to parse {json_file}: {e}")
                continue

        # Get schemas from YAML (look for entity name or NewRequest name)
        yaml_schemas = yaml_obj.get("components", {}).get("schemas", {})
        yaml_schema_def = (
            yaml_schemas.get(f"{entity_name}NewRequest")
            or yaml_schemas.get(entity_name)
            or {}
        )

        nullable_yaml_props = collect_nullable_yaml_properties(yaml_schema_def)
        if not nullable_yaml_props:
            continue

        # Get properties from JSON entity
        json_entity_def = json_obj.get("$defs", {}).get(entity_name, {})
        json_props = json_entity_def.get("properties", {})

        issues = []  # list of (json_prop_name, yaml_prop_name)
        seen_json_props = set()
        for prop_name, yaml_prop_def in nullable_yaml_props.items():
            # Check direct name match
            if prop_name in json_props:
                if prop_name not in seen_json_props and not is_nullable_in_json(json_props[prop_name]):
                    issues.append((prop_name, prop_name))
                    seen_json_props.add(prop_name)
                continue

            # Check derived relationship name (e.g. programDbId -> program)
            rel_name = derive_json_rel_name(prop_name)
            if rel_name and rel_name in json_props:
                if rel_name not in seen_json_props and not is_nullable_in_json(json_props[rel_name]):
                    issues.append((rel_name, prop_name))
                seen_json_props.add(rel_name)

        if issues:
            total_issues += len(issues)
            print(f"\n[{entity_name}]  YAML: {os.path.relpath(yaml_file, root)}  |  JSON: {os.path.relpath(json_file, root)}")
            for json_prop_name, yaml_prop_name in issues:
                yaml_type = yaml_schema_def["properties"][yaml_prop_name].get("type", "object/$ref")
                json_type = json_props[json_prop_name].get("type", "$ref")
                label = json_prop_name if json_prop_name == yaml_prop_name else f"{json_prop_name} (from yaml:{yaml_prop_name})"
                print(f"  MISMATCH  '{label}'  yaml_type={yaml_type}  json_type={json_type}")

            if fix_mode:
                for json_prop_name, yaml_prop_name in issues:
                    json_props[json_prop_name] = make_nullable_in_json(json_props[json_prop_name])
                    print(f"    FIXED  '{json_prop_name}'")
                    total_fixed += 1

                with open(json_file, "w", encoding="utf-8") as f:
                    json.dump(json_obj, f, indent=4, ensure_ascii=False)
                    f.write("\n")

    print(f"\n{'='*60}")
    print(f"Total mismatches found: {total_issues}")
    if fix_mode:
        print(f"Total fixes applied:    {total_fixed}")
    else:
        print("Run with --fix to apply corrections.")


if __name__ == "__main__":
    main()
