FROM python:3.9-slim-bullseye
WORKDIR /app
#ENV APP_PATH=services/worker
COPY . .
ADD config.json .
ADD utils.py .
RUN pip install -r services/bot/requirements.txt

CMD ["python3", "services/worker/app.py"]