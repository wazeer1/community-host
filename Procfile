# web: guncorn community.wsgi
web: gunicorn --pythonpath project community.wsgi:application --access-logfile -
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput 