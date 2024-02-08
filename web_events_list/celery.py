import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_events_list.settings')

app = Celery('web_events_list')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
