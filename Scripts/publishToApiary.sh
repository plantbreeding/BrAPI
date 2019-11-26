#!/bin/bash
# Param 1: compiled blueprint file (default "$HOME/brapi_blueprint.apib")
# Param 2: name of the apiary api (default "brapi")

if [ -f "$1" ]; then
	BRAPI_FILE=${1};
else
	BRAPI_FILE=${HOME}/brapi_blueprint.apib;
fi
if [ -z "$2" ]; then
	echo "usage: 'publishToApiary <blueprint file> <apiary name> <apiary key>"
	exit 1
else
	APINAME=${2}
fi
if [ -z "$3" ]; then
	echo "usage: 'publishToApiary <blueprint file> <apiary name> <apiary key>"
	exit 1
else
	APIARY_TOKEN=${3}
fi


# Publish to apiary
echo
echo $BRAPI_FILE
echo $APINAME
echo

curl -si \
  --request POST \
  --header "Authentication:Token $APIARY_TOKEN" \
  --header "content-type:application/json; charset=utf-8" \
  --data-binary @$BRAPI_FILE \
  https://api.apiary.io/blueprint/publish/$APINAME 

if [ $? -ne 0 ]; then
	echo
	echo "ERROR: Apiary rejected the file"
	exit 1
fi