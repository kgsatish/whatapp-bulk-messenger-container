# syntax=docker/dockerfile:1
FROM python:3.9.2

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
#ENV SELENIUM_URL $SELENIUM_URL
#ENV IDENTITY_TOKEN $IDENTITY_TOKEN
EXPOSE 8080

# Copy files
WORKDIR /app
COPY whatsapp.py whatsapp.py
COPY requirements.txt requirements.txt

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 whatsapp:app
