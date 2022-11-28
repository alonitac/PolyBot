FROM python:3.9-slim-bullseye
WORKDIR /app
COPY config.json .
COPY utils.py .
COPY . .
RUN pip install -r services/bot/requirements.txt

CMD ["python3", "services/worker/app.py"]