###CELERY
from celery import shared_task
import time

@shared_task(queue='queueshort')
def taskshort():
    print('in django, short')
    time.sleep(1)
    return

@shared_task(queue='queuelong')
def tasklong():
    print('in django, long start')
    time.sleep(10)
    print('in django, long end')
    return