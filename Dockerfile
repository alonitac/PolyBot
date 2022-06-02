FROM python:3.8.12-slim-buster
COPY bot.py .
COPY utils.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

# YOUR COMMANDS HERE
# ....
# ....

CMD ["python3", "bot.py"]