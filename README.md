# tdd-with-python

## Prerequisites

1. Docker installed

2. [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) installed - set up VNC connection with browser session

## Usage

1. Clone the repo

1. Build the Docker image and start all services:

        $ docker-compose up --build

1. Run the test suite:

        $ docker-compose run --rm web sh -c 'python -W ignore test/* '
    Note: To visually see what the browser is doing you will need to create connection to VNC Server `localhost:5900`
