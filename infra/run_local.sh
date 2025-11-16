#!/usr/bin/env bash
# run_local.sh - build and run the docker image locally
set -e
IMAGE_NAME=nlp-model:dev


docker build -t $IMAGE_NAME .
docker run --rm -p 8080:8080 -p 8000:8000 $IMAGE_NAME