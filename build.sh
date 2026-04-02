#!/usr/bin/env bash
# Exin on error
set -0 errexit

# Modify this line as needed for your package manager (pip. poetry, etc.)
pip install -r requirements.txt

# Convert static assets files
python manage.py collectstatic --noinput

# Apply any outstanding database migrations
python manage.py migrate
