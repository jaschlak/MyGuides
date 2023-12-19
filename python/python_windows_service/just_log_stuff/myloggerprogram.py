# -*- coding: utf-8 -*-

import time
from support.log import LogClass
import datetime



def write_to_logs():

    Log = LogClass()

    last_time = time.time()

    Log.logger.info('Starting Service at: {}'.format(datetime.datetime.now()))

    while True:
        
        if time.time() - last_time > 5:
            
            Log.logger.info('last_update: {}'.format(datetime.datetime.now()))
            last_time = time.time()