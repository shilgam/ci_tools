# tdd-with-python

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

1. Run the test suite:

        $ docker-compose --project-name tests --file docker-compose.test.yml up --abort-on-container-exit
    Note: To visually see what the browser is doing you will need to create connection to VNC Server `localhost:5900`
