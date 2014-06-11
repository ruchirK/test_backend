from __future__ import absolute_import
__author__ = 'ruchir'

from celery import Celery
celery = Celery(include=['twitter.tasks'])

celery.config_from_object('celeryconfig')

if __name__ == '__main__':
    celery.start()
