FROM python:3.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY app.py ./app.py
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]