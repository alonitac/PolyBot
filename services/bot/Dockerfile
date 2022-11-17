FROM python:3.10-slim-bullseye
WORKDIR /app
ENV APP_PATH=services/bot
COPY . .
RUN pip install -r requirements.txt

CMD ["python3", "services/bot/app.py"]