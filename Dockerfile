FROM python:3.7-alpine AS builder

WORKDIR /build

COPY requirements.txt ./requirements.txt
COPY setup.py ./setup.py
COPY helloworld/ ./helloworld

RUN python setup.py bdist_wheel

FROM python:3.7-alpine
COPY --from=builder /build/dist /tmp/dist

RUN pip install /tmp/dist/*
RUN rm -rf /tmp/dist

ARG version
ENV VERSION=$version

ENTRYPOINT ["hello-world"]