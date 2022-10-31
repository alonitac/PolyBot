FROM python:3.8.15-slim-buster

WORKDIR /app/

COPY . /app

RUN apt-get update \
    && apt-get install expat \

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \


CMD ["python3", "worker.py"]