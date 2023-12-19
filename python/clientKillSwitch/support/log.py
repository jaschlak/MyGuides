# -*- coding: utf-8 -*-

import os
import logging
from logging import handlers


class LogClass:
    
    def __init__(self):
        
        folderpath = 'C:\Logs'
        
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        
        LOG_FILENAME = folderpath + "/python_service.log"
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        # important, handlers are global, this gets rid of old handlers
        handlers = logger.handlers[:]
        for handler in handlers:
            handler.close()
            logger.removeHandler(handler)
        
        handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=100000000, backupCount=20)
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        logger.addHandler(handler)
        
        self.logger = logger