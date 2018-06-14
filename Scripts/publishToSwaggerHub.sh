#!/bin/bash

# Param 1: compiled OpenAPI file (default "$HOME/brapi_blueprint.apib")

if [ -f "$1" ]; then
	BRAPI_FILE=${1};
else
	BRAPI_FILE=${HOME}/brapi_openapi.yaml;
fi

# Publish to apiary
echo $BRAPI_FILE

curl -i \
  --request POST \
  --header "Authorization:Bearer $SWAGGERHUB_TOKEN" \
  --header "content-type:application/yaml; charset=utf-8" \
  --data-binary @$BRAPI_FILE \
  https://api.swaggerhub.com/apis/PlantBreedingAPI/BrAPI

if [ $? -ne 0 ]; then
	echo "ERROR: SwaggerHub rejected the file"
	exit 1
fi