PROJ_FILE := project.json
APP_VERSION := $(shell cat ${PROJ_FILE} | jq .version)

.PHONY: build run deploy

build:
	docker image build --tag helloworld:latest --build-arg version=${APP_VERSION} .

run: build
	docker container run --publish 8080:8080 helloworld:latest

deploy:
	kubectl apply -f service.yaml
	kubectl apply -f deployment.yaml
	kubectl apply -f hpa.yaml

delete:
	kubectl delete svc hello-world
	kubectl delete deploy hello-world
	kubectl delete hpa hello-world