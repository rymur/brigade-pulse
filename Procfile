web: gunicorn settings.wsgi_settings --log-file -
worker: celery worker --app=celery_worker.app -l info --beat
