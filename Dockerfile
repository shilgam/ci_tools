FROM python:3.6.1-alpine

RUN pip install Flask \
                pytest

COPY . /usr/src/

WORKDIR /usr/src/app
