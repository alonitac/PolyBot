FROM python:3.8.12-slim-buster
LABEL maintainer="poratnick@gmail.com"
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
CMD ["python3", "bot.py"]