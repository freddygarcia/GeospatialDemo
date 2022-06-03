python -m app.core.initialize_db
gunicorn -b 0.0.0.0:5000 wsgi:app