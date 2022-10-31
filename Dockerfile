FROM python:3.8.15-slim-buster

WORKDIR /app/

COPY . /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \

RUN apt-get update \
    && apt-get install expat \

CMD ["python3", "worker.py"]