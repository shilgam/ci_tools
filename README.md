# ci_tools

[![Build Status](https://travis-ci.com/shilgam/ci_tools.svg?branch=master)](https://travis-ci.com/shilgam/ci_tools) [![pipeline status](https://gitlab.com/shilgam1/ci_tools/badges/master/pipeline.svg)](https://gitlab.com/shilgam1/ci_tools/commits/master) [![Codeship Status for shilgam/ci_tools](https://app.codeship.com/projects/84dc83c0-1686-0137-368c-02228243811b/status?branch=master)](https://app.codeship.com/projects/327923) [![CircleCI](https://circleci.com/gh/shilgam/ci_tools.svg?style=svg)](https://circleci.com/gh/shilgam/ci_tools)

Popular CI/CD Tools Comparison: Travis, CircleCI, Gitlab CI, Codeship Pro

[Slides](https://shilgam.github.io/reveal.js/slides/ci_tools/)

## Prerequisites

Docker and docker-compose installed

## Usage

1. Clone the repo

1. Build the Docker image and start app services:

        $ docker-compose up --build

1. Launch the app: http://0.0.0.0:5000/

1. Stop app services and remove containers:

        $ docker-compose down

### Run the test suite

1. Run tests

        $ docker-compose run --rm web
