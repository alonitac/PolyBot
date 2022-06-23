FROM python:3.8.12-alpine
LABEL maintainer="poratnick@gmail.com"
RUN apk add --update python3 npm curl
RUN pip install -r requirements.txt
WORKDIR /src
COPY . /src
RUN npm install
EXPOSE 8080
CMD ["python3", "./bot.py"]