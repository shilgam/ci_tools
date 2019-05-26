FROM python:3.6.1-alpine

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN pip install Flask \
                pytest

ENV PYTHONUNBUFFERED 1

COPY . /usr/src/

CMD python main.py
