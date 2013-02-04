FROM python:3.6.1-alpine

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY . .
