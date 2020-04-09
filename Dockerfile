FROM python:3.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY app.py ./app.py
RUN pip install -r requirements.txt
ARG version
ENV VERSION=$version
ENTRYPOINT ["python", "app.py"]