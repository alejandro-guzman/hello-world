#!/bin/bash

docker image build -t helloworld --build-arg version=v0.2.1 .
docker container run -p 8080:8080 -e MONGO_HOST=mongo helloworld