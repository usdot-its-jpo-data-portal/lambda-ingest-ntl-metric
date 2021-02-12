#!/bin/bash

# NOTE!
# This script is deprecated and was intended for manual deployment packaging.
rm lambda-ingest-ntl-metric.zip
mkdir _package
pip install -r requirements.txt --upgrade --target _package
cp src/* _package/
cd _package/
zip -r ../lambda-ingest-ntl-metric.zip *
cd ..
rm -rf _package/
echo "Created package in lambda-ingest-ntl-metric.zip"
