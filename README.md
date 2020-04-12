# hello-world

Example flask application running in Kubernetes

Find on [Dockerhub](https://hub.docker.com/r/alejandroguzman/helloworld)

## Development

Clone repo

```bash
git clone git@github.com:alejandro-guzman/hello-world.git
```

Build docker image

```bash
make build
```

Run docker container

```bash
make run
```

Deploy to Kubernetes

```bash
make deploy
```
