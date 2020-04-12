PROJ_FILE := project.json
APP_VERSION := $(shell cat ${PROJ_FILE} | jq .version)

.PHONY: build run

build:
	docker image build --tag helloworld:latest --build-arg version=${APP_VERSION} .

run: build
	docker container run --publish 8080:8080 helloworld:latest

mkdeploy:
	kubectl apply -f service.yaml
	kubectl apply -f deployment.yaml