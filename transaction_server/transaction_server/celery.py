import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "transaction_server.settings")

app = Celery("transaction_server")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()