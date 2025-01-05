#!/bin/ash
echo "appl database migration"
python manage.py migrate

exec "$@"