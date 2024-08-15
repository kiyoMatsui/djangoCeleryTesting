# from __future__ import absolute_import
###CELERY
import os

from celery import Celery
#from django.conf import settings


# copied from manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
# new instance
app = Celery("dcelery")
# tell celery about django settings with namespace CELERY_
app.config_from_object("django.conf:settings", namespace="CELERY")

#app.conf.task_routes = {'newapp.tasks.task1': {'queue':'queue1'}, 'newapp.tasks.task2': {'queue':'queue2'}} # if not set in the decorator

#look for tasks.py in installed apps.
app.autodiscover_tasks()


#app.conf.beat_schedule = app.conf.CELERY_BEAT_SCHEDULE
#app.conf.broker_transport_options = {"visibility_timeout": 60 * 60 * 24}  # 1 day
# http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#redis-caveats

# setting this to settings.py file only is not respected. Setting here too
#app.conf.task_always_eager = settings.CELERY_TASK_ALWAYS_EAGER


#app.conf.worker_prefetch_multiplier = 1
