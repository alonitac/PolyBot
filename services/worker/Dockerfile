FROM python:3.9-slim-bullseye
WORKDIR /app
COPY . .
RUN pip install -r services/worker/requirements.txt

CMD ["python3", "services/worker/app.py"]