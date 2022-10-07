FROM python:3.9-slim
LABEL app=bot
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt

CMD ["python3", "bot.py"]
