#!/bin/sh
set -e

# Wait for services to be started
dockerize -wait http://web:8000 \
          -wait http://hub:4444 \
          -wait http://chrome-debug:5555 \
          -wait http://firefox:5555 \
          -timeout 20s

exec "$@"
