# -*- coding: utf-8 -*-

CELERY_RESULT_BACKEND = "database"
CELERY_RESULT_DBURI = "mssql+pyodbc://<user>:<password>@<mssql_host>/<mssqldb>?driver=SQL+Server"
CELERY_TASK_SERIALIZER = "json"

CELERY_IMPORTS = ('tasks')
CELERY_IGNORE_RESULT = False

BROKER_HOST = "<rabbit host>"
BROKER_PORT = 5672
BROKER_VHOST = "/"
BROKER_USER = "<rabbit_user>"
BROKER_PASSWORD = "<rabbit_pass>"
BROKER_URL = 'amqp://'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'doctor-every-10-seconds': {
        'task': 'tasks.fav_doctor',
        'schedule': timedelta(seconds=10)
        },
    }