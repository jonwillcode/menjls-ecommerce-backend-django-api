web: gunicorn bakery_django.wsgi --log-file - --log-level debug
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic
release: python manage.py migrate --noinput