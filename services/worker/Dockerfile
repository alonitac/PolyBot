FROM python:3.9-slim-bullseye
WORKDIR /app
RUN pip install -r services/worker/requirements.txt

COPY . .

CMD ["python3", "services/worker/app.py"]