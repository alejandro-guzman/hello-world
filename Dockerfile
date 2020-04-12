ARG py_version
FROM python:${py_version}-alpine AS builder

WORKDIR /build

COPY requirements.txt ./requirements.txt
COPY project.json ./project.json
COPY README.md ./README.md
COPY setup.py ./setup.py
COPY helloworld/ ./helloworld

RUN pip install --upgrade pip setuptools wheel

RUN python setup.py bdist_wheel

FROM python:${py_version}-alpine
COPY --from=builder /build/dist /tmp/dist

RUN pip install --compile /tmp/dist/*
RUN rm -rf /tmp/dist

ARG version
ENV VERSION=$version

ENTRYPOINT ["hello-world"]