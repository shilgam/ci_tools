# ci_tools

[![Build Status](https://travis-ci.com/shilgam/tdd-with-python.svg?branch=master)](https://travis-ci.com/shilgam/tdd-with-python) [![pipeline status](https://gitlab.com/shilgam1/ci_tools/badges/master/pipeline.svg)](https://gitlab.com/shilgam1/ci_tools/commits/master) [![Codeship Status for shilgam/ci_tools](https://app.codeship.com/projects/84dc83c0-1686-0137-368c-02228243811b/status?branch=master)](https://app.codeship.com/projects/327923) [![CircleCI](https://circleci.com/gh/shilgam/ci_tools.svg?style=svg)](https://circleci.com/gh/shilgam/ci_tools)

## Prerequisites

1. Docker installed

2. [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) installed - set up VNC connection with browser session

## Usage

1. Clone the repo

1. Build the Docker image and start all services:

        $ docker-compose up --build

1. Launch the app: http://0.0.0.0:8000/

1. Stop all services and remove containers:

        $ docker-compose down

1. Run the test suite

    1. Functional tests

        1. run tests:

                $ docker-compose --file docker-compose.test.yml run --rm web
            Notes:
            - To visually see what the browser is doing you will need to create connection to VNC Server `localhost:5900`
            - Selenium Grid URL: http://0.0.0.0:4444/

        1. clean up after tests:

                $ docker-compose --file docker-compose.test.yml down

    1. Unit tests

            $ docker-compose run --rm web python manage.py test lists
