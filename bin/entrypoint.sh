#!/bin/sh

# python manage.py test
# python manage.py makemigrations
# python manage.py migrate

set -e

echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  entrypoint.sh"
echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  python manage.py runserver 0.0.0.0:8000"
# python manage.py runserver 0.0.0.0:8000
# sleep 4
exec "$@"
