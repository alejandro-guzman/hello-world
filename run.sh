#!/bin/bash

docker image build -t helloworld .
docker container run -p 8080:8080 helloworld