from celery import shared_task
import time
# seems like file and dir names must match what we see in django app

@shared_task(queue='queueshort')
def taskshort():
    print('in worker, short')
    time.sleep(1)
    return

@shared_task(queue='queuelong')
def tasklong():
    print('in worker, long start')
    time.sleep(10)
    print('in worker, long end')
    return