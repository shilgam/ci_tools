FROM python:3.6.1-alpine

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

RUN pip install Flask \
                pytest

COPY . /usr/src/

CMD python helloapp.py
