# Import the base image

FROM python:3.8.5-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
