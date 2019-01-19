#!/bin/sh
set -e

# Wait for services to be started
dockerize -wait http://web:8000 \
          -wait http://hub:4444 \
          -timeout 5s

exec "$@"
