FROM python:3.8.12-slim-buster
LABEL app=bot
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
CMD ["python3", "bot.py"]
