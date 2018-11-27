#!/usr/bin/env bash

NAME=`grep name dslink.json | head -1 | awk '{ print $2 }' | tr -d '","'`
if [ -z "${NAME}" ]; then
    echo "Cannot determinate name from dslink.json" 1>&2
    exit 1
fi

VERSION=`grep version dslink.json | awk '{ print $2 }' | tr -d '","'`
if [ -z "${VERSION}" ]; then
    echo "Cannot determinate version from dslink.json" 1>&2
    exit 1
fi


zip ./${NAME}_${VERSION}.zip -r src dslink.json setup.py

echo "Created " `pwd`/"${NAME}_${VERSION}.zip"
