# from __future__ import absolute_import
###CELERY
from .celery import app as celery_app

# when django instance, this will be run and find the celery app
__all__ = ("celery_app",)