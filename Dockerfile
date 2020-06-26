FROM python:3.7-alpine

# Unbuffer Python logs
ENV PYTHONUNBUFFERED=1

RUN apk add bash

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
