FROM python:3.8-slim

WORKDIR /app

RUN pip install flask redis

COPY . .



CMD [ "python", "app.py"]