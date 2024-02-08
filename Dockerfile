FROM python:3.11-alpine
LABEL authors="kras"

WORKDIR /usr/src/example_events

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add python3-dev && apk cache clean

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

