FROM python:3.8-slim-bullseye
WORKDIR /yt_down_bot
LABEL app=bot
COPY . .
RUN pip install -r requirements.txt

FROM python:3.9-slim
LABEL app=bot
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
CMD ["python3", "bot.py"]
