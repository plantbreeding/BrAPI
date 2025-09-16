#!/bin/bash -e

echo
echo
echo "Check python packages"
returnval=`python3 -c 'import pkgutil; print(1 if pkgutil.find_loader("SpellChecker") else 0)'`
if [[ "$returnval" -ne 1 ]]; then pip3 install pyspellchecker; fi

mkdir -p ./build/results

echo
echo
echo "Spell Check Run"
echo "Spell checking BrAPI-Core"
echo "BrAPI-Core" >> ./build/results/spellingResults.txt
python3 ./Scripts/checkSpelling.py "./Specification/BrAPI-Core/" >> ./build/results/spellingResults.txt
echo "Spell checking BrAPI-Germplasm"
echo "BrAPI-Germplasm" >> ./build/results/spellingResults.txt
python3 ./Scripts/checkSpelling.py "./Specification/BrAPI-Germplasm/" >> ./build/results/spellingResults.txt
echo "Spell checking BrAPI-Phenotyping"
echo "BrAPI-Phenotyping" >> ./build/results/spellingResults.txt
python3 ./Scripts/checkSpelling.py "./Specification/BrAPI-Phenotyping/" >> ./build/results/spellingResults.txt
echo "Spell checking BrAPI-Genotyping"
echo "BrAPI-Genotyping" >> ./build/results/spellingResults.txt
python3 ./Scripts/checkSpelling.py "./Specification/BrAPI-Genotyping/" >> ./build/results/spellingResults.txt
echo "Spell checking Components"
echo "Components" >> ./build/results/spellingResults.txt
python3 ./Scripts/checkSpelling.py "./Specification/Components/" >> ./build/results/spellingResults.txt


echo
echo
echo "Build OpenAPI YAML files per domain: ./brapi_openapi.yaml"
echo "Building BrAPI-Core"
python3 ./Scripts/buildOpenAPI.py "./Specification/BrAPI-Core/" "./Specification/Components/" "./Specification/BrAPI-Germplasm/" >> ./build/results/buildOpenAPIBrAPI-CoreResults.txt
echo "Building BrAPI-Germplasm"
python3 ./Scripts/buildOpenAPI.py "./Specification/BrAPI-Germplasm/" "./Specification/Components/" >> ./build/results/buildOpenAPIBrAPI-GermplasmResults.txt
echo "Building BrAPI-Phenotyping"
python3 ./Scripts/buildOpenAPI.py "./Specification/BrAPI-Phenotyping/" "./Specification/Components/" >> ./build/results/buildOpenAPIBrAPI-PhenotypingResults.txt
echo "Building BrAPI-Genotyping"
python3 ./Scripts/buildOpenAPI.py "./Specification/BrAPI-Genotyping/" "./Specification/Components/" "./Specification/BrAPI-Germplasm/" >> ./build/results/buildOpenAPIBrAPI-GenotypingResults.txt

echo
echo
echo "Build README files"
echo "Building BrAPI-Core README files"
echo "BrAPI-Core" >> ./build/results/buildREADMEBrAPI-CoreResults.txt
python3 ./Scripts/buildReadMes.py "./Specification/BrAPI-Core/" >> ./build/results/buildREADMEBrAPI-CoreResults.txt
echo "Building BrAPI-Germplasm README files"
echo "BrAPI-Germplasm" >> ./build/results/buildREADMEBrAPI-GermplasmResults.txt
python3 ./Scripts/buildReadMes.py "./Specification/BrAPI-Germplasm/" >> ./build/results/buildREADMEBrAPI-GermplasmResults.txt
echo "Building BrAPI-Phenotyping README files"
echo "BrAPI-Phenotyping" >> ./build/results/buildREADMEBrAPI-PhenotypingResults.txt
python3 ./Scripts/buildReadMes.py "./Specification/BrAPI-Phenotyping/" >> ./build/results/buildREADMEBrAPI-PhenotypingResults.txt
echo "Building BrAPI-Genotyping README files"
echo "BrAPI-Genotyping" >> ./build/results/buildREADMEBrAPI-GenotypingResults.txt
python3 ./Scripts/buildReadMes.py "./Specification/BrAPI-Genotyping/" >> ./build/results/buildREADMEBrAPI-GenotypingResults.txt

echo
echo
echo "Build BluePrint MD file: ./brapi_blueprint.apib ./brapi_blueprint.apib.json"
echo "Build BluePrint MD for BrAPI-Core"
python3 ./Scripts/buildBlueprint.py -out "./Specification/BrAPI-Core/" -header "./Specification/BrAPI-Core/swaggerMetaData.yaml" -source "./Specification/BrAPI-Core/" >> ./build/results/buildBlueprintResults.txt
echo "Build BluePrint MD for BrAPI-Germplasm"
python3 ./Scripts/buildBlueprint.py -out "./Specification/BrAPI-Germplasm/" -header "./Specification/BrAPI-Germplasm/swaggerMetaData.yaml" -source "./Specification/BrAPI-Germplasm/" >> ./build/results/buildBlueprintResults.txt
echo "Build BluePrint MD for BrAPI-Phenotyping"
python3 ./Scripts/buildBlueprint.py -out "./Specification/BrAPI-Phenotyping/" -header "./Specification/BrAPI-Phenotyping/swaggerMetaData.yaml" -source "./Specification/BrAPI-Phenotyping/" >> ./build/results/buildBlueprintResults.txt
echo "Build BluePrint MD for BrAPI-Genotyping"
python3 ./Scripts/buildBlueprint.py -out "./Specification/BrAPI-Genotyping/" -header "./Specification/BrAPI-Genotyping/swaggerMetaData.yaml" -source "./Specification/BrAPI-Genotyping/" >> ./build/results/buildBlueprintResults.txt

echo
echo
echo "Build complete OpenAPI in one YAML file: ./brapi_openapi.yaml for sharing."
python3 ./Scripts/buildOpenAPI.py ./Specification/swaggerMetaData.yaml ./Specification/BrAPI-Core/ ./Specification/BrAPI-Germplasm/ ./Specification/BrAPI-Genotyping/ ./Specification/BrAPI-Phenotyping/ ./Specification/Components >> ./build/results/buildOpenAPICompleteResults.txt

cp ./Specification/BrAPI-Core/brapi_openapi.yaml ./build/brapi_openapi.yaml
echo "Complete OpenAPI in one YAML file can be found here:"
realpath ./build/brapi_openapi.yaml

echo "Build completed successfully. Please check the /build/results directory for any warnings"