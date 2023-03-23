#!/bin/bash

echo "Waiting for postgres..."

sleep 30

#while ! curl http://$POSTGRES_PORT_5432_TCP_ADDR:$POSTGRES_PORT_5432_TCP_PORT/ 2>&1 | grep '52'
#do
#  sleep 1
#done

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
exec "$@"

