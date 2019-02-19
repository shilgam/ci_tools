#!/bin/sh
set -e

# Wait for services to be started
dockerize -wait http://chrome:5555 \
          -wait http://chrome2:5555 \
          -timeout 20s

exec "$@"
