FILE := project.json
PY_VERSION := $(shell cat ${FILE} | jq .py_version)
APP_VERSION := $(shell cat ${FILE} | jq .version) 

.PHONY: build run

build:
	docker image build --tag helloworld:latest \
		--build-arg py_version=${PY_VERSION} \
		--build-arg version=${APP_VERSION} .

run: build
	docker container run --publish 8080:8080 helloworld:latest

deploy:
	minikube kubectl -- apply -f deploy/*