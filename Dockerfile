FROM python:3.8.12-alpine
RUN pip install -r requirements.txt
WORKDIR /code
COPY . .
EXPOSE 5000
CMD ["python3", "bot.py"]