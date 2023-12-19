# -*- coding: utf-8 -*-

import os
import logging
from logging import handlers
import time
import datetime
import threading


class LogClass:
    
    def __init__(self):
        
        folderpath = 'C:\Logs'
        filename = 'python_test.log'
        LOGFILEPATH = '/'.join([folderpath,filename])
        
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        # important, handlers are global, this gets rid of old handlers
        handlers = logger.handlers[:]
        for handler in handlers:
            handler.close()
            logger.removeHandler(handler)
        
        handler = logging.handlers.RotatingFileHandler(LOGFILEPATH, maxBytes=100000000, backupCount=20)
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        logger.addHandler(handler)
        
        self.logger = logger
  
def log_entries():
    
    Log = LogClass()
    
    last_time = time.time()
    
    Log.logger.info('Starting Service at: {}'.format(datetime.datetime.now()))
    
    while True:
    
        if time.time() - last_time > 5:
            
            Log.logger.info('last_update: {}'.format(datetime.datetime.now()))
            last_time = time.time()
  
if __name__ == '__main__':

    x = threading.Thread(target=log_entries, args=())
    x.start()