#!/bin/bash


# Param 1: compiled OpenAPI file (default "$HOME/brapi_blueprint.apib")

if [ -z "$1" ]; then
	echo "usage: 'publishToSwaggerHub <blueprint file> <apiary name> <apiary key>"
	exit 1
else
	BRAPI_FILE=${1};
fi
if [ -z "$2" ]; then
	echo "usage: 'publishToSwaggerHub <blueprint file> <apiary name> <apiary key>"
	exit 1
else
	APINAME=${2}
fi
if [ -z "$3" ]; then
	echo "usage: 'publishToSwaggerHub <blueprint file> <apiary name> <apiary key>"
	exit 1
else
	SWAGGERHUB_TOKEN=${3}
fi

# Publish to apiary
echo $BRAPI_FILE

curl -i \
  --request POST \
  --header "Authorization:Bearer $SWAGGERHUB_TOKEN" \
  --header "content-type:application/yaml; charset=utf-8" \
  --data-binary @$BRAPI_FILE \
  https://api.swaggerhub.com/apis/PlantBreedingAPI/$APINAME

if [ $? -ne 0 ]; then
	echo "ERROR: SwaggerHub rejected the file"
	exit 1
fi