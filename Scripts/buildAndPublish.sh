#!/bin/bash

## You'll need to get a token (https://login.apiary.io/tokens)
## Storing the key in $ROOT_DIRECTORY/.bash_rc
source ${HOME}/.bash_rc

#---------------------------------------------------------------------------------------
# Build and publish dev
DEV_PACKAGE_DIR=${HOME}/BRAPI/DEV
DEV_APIARY_NAME=brapidev

if [ -d "$DEV_PACKAGE_DIR/API" ]; then
    cd $DEV_PACKAGE_DIR/API
    git pull
else
    cd $DEV_PACKAGE_DIR
    git clone https://github.com/plantbreeding/API.git -b master --single-branch
fi

BLUEPRINT_FILE=`${DEV_PACKAGE_DIR}/API/Scripts/buildBrapiBlueprint.sh ${DEV_PACKAGE_DIR}`

${DEV_PACKAGE_DIR}/API/Scripts/publishToApiary.sh $BLUEPRINT_FILE $DEV_APIARY_NAME


#---------------------------------------------------------------------------------------
# Build and publish latest release
PROD_PACKAGE_DIR=${HOME}/BRAPI/PROD
PROD_APIARY_NAME=brapi

LATEST_REL_NUM=`curl -s https://github.com/plantbreeding/API/releases/latest | sed -r "s#.*V([0-9]\.[0-9]).*#\1#"`
LATEST_REL_URL="https://codeload.github.com/plantbreeding/API/zip/V$LATEST_REL_NUM"
echo $LATEST_REL_URL

rm $PROD_PACKAGE_DIR/archive.zip
if [ -d "$PROD_PACKAGE_DIR/API-${LATEST_REL_NUM}" ]; then
    rm -rf $PROD_PACKAGE_DIR/API-${LATEST_REL_NUM};
fi

curl $LATEST_REL_URL > $PROD_PACKAGE_DIR/archive.zip

unzip $PROD_PACKAGE_DIR/archive.zip -d $PROD_PACKAGE_DIR

BLUEPRINT_FILE=`${PROD_PACKAGE_DIR}/API-${LATEST_REL_NUM}/Scripts/buildBrapiBlueprint.sh ${PROD_PACKAGE_DIR}`

${PROD_PACKAGE_DIR}/API-${LATEST_REL_NUM}/Scripts/publishToApiary.sh $BLUEPRINT_FILE $PROD_APIARY_NAME


#---------------------------------------------------------------------------------------
# Build and publish prev release