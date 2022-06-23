# Group Reference Sets

From GA4GH Variants schema documentation

A reference genome is a genome assembly that other genomes are compared to and described with respect to. For example, sequencing reads are mapped to and described with respect to a reference genome in the API, and genetic variations are described as edits to reference scaffolds/contigs. In the API a reference genome is described by a ReferenceSet. In turn a ReferenceSet is composed of a set of Reference objects, each which represents a scaffold or contig in the assembly. Reference sequences are expected to have unique names within a ReferenceSet