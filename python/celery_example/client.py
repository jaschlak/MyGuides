# -*- coding: utf-8 -*-

# https://www.youtube.com/watch?v=waD4MEj8WGw

from celery import Celery

celery = Celery()
celery.config_from_object('celeryconfig')