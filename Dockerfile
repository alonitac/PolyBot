FROM python:3.8.12-slim-buster
WORKDIR /yt_down_bot
COPY . .
RUN pip install -r requirements.txt

CMD ["python3", "bot.py"]