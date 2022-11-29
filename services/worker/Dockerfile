FROM python:3.9-slim-bullseye
WORKDIR /app
ADD services/worker/requirements.txt .
ADD services/worker/config.json .
ADD services/worker/utils.py .
ENV APP_PATH=services/worker
COPY . .
RUN pip install -r $APP_PATH/requirements.txt

CMD ["python3", "services/worker/app.py"]