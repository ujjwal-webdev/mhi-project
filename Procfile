web: gunicorn MHI9.wsgi:application --log-file - --log-level debug
python3 manage.py collectstatic --noinput
manage.py migrate