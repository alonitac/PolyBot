FROM python:3.8.12-slim-buster
COPY . /src/app
WORKDIR /src/app
RUN pip3 install boto3
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python3", "bot.py"]