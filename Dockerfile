FROM python:3.6.1-alpine

# Install dockerize (https://github.com/jwilder/dockerize)
RUN apk add --no-cache openssl
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./app/requirements.txt .

RUN apk add --no-cache --virtual build-dependencies build-base libffi-dev openssl-dev \
    # fabric3 deps
    && pip install -r requirements.txt \
    && apk del build-dependencies

ENV PYTHONUNBUFFERED 1

COPY . /usr/src/

# TODO: fix permission issue in Travis
## Run the image as a non-root user
# RUN adduser -D myuser
# USER myuser

# Expose is NOT supported by Heroku
# EXPOSE 5000

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD gunicorn --bind 0.0.0.0:$PORT superlists.wsgi
