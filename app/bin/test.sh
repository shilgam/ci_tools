#!/bin/sh
set -e

# Wait for services to be started
dockerize -wait http://chrome:5555 \
          -wait http://chrome2:5555 \
          -wait http://chrome3:5555 \
          -wait http://chrome4:5555 \
          -wait http://chrome5:5555 \
          -wait http://chrome6:5555 \
          -wait http://chrome7:5555 \
          -wait http://chrome8:5555 \
          -wait http://chrome9:5555 \
          -wait http://chrome10:5555 \
          -wait http://chrome11:5555 \
          -wait http://chrome12:5555 \
          -timeout 20s

exec "$@"
