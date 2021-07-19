
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time


@shared_task
def add(x, y):
    time.sleep(10)
    return x + y


@shared_task
def mul(x, y):
    time.sleep(5)
    return x * y

@shared_task
def Sleepy(duration):
    time.sleep(duration)
    return None
#From notifications.tasks import add