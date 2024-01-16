import logging

from time import sleep

from celery import shared_task

from event.serializers import EventSerializer

logger = logging.getLogger(__name__)

@shared_task
def event_save(data, *args, **kwargs):
    sleep(60)

    event_serialize = EventSerializer(data=data)
    if event_serialize.is_valid():
        event_serialize.create(event_serialize.validated_data)
    else:
        logger.info("Ошибочка в данных: %s" % data)
