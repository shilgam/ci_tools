# tdd-with-python

[![Build Status](https://travis-ci.com/shilgam/tdd-with-python.svg?branch=master)](https://travis-ci.com/shilgam/tdd-with-python)

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

    1. Functional tests:

            $ docker-compose --project-name functests --file docker-compose.test.yml up --abort-on-container-exit
        Note: To visually see what the browser is doing you will need to create connection to VNC Server `localhost:5900`

    1. Unit tests:

            $ docker-compose run web python manage.py test lists

## Deploy to Heroku

1. Make sure you have a working Docker installation (eg. `docker ps`) and that you’re logged in to Heroku (`heroku login`).

1. Log in to Container Registry:

        $ heroku container:login

1. Navigate to the app’s directory and create a Heroku app:

        $ heroku create        
        Creating salty-fortress-4191... done, stack is cedar-14
        https://salty-fortress-4191.herokuapp.com/ | https://git.heroku.com/salty-fortress-4191.git

1. Build the image and push to Container Registry:

        $ heroku container:push web

1. Then release the image to your app:

        $ heroku container:release web

1. Now open the app in your browser:

        $ heroku open
