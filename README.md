# tdd-with-python

## Usage

1. Clone the repo

1. Build the Docker image and start all services:

        $ docker-compose up --build

1. Run the test suite:

        $ docker-compose run --rm web sh -c 'python -W ignore test/*'
