#!/bin/bash
set -e

echo "Creating staticfiles directory..."
mkdir -p staticfiles

echo "Running collectstatic..."
python manage.py collectstatic --noinput --clear

echo "Running migrations..."
python manage.py migrate

echo "Starting gunicorn..."
exec gunicorn core.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --log-level info
