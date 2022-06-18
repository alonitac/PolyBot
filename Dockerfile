FROM python:3.8.12-slim-buster

# YOUR COMMANDS HERE
# ....
# ....
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "bot.py"]