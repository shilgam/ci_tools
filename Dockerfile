FROM python:3.6.1-alpine

RUN pip install Flask \
                pytest

WORKDIR /usr/src/

COPY . .
