# Logging

    Code for logging
    
## Rolling Logs based on file size



    import logging

    class LogClass:
        
        def __init__(self):
            LOG_FILENAME = "Log/test_log.log"
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            
            # important, handlers are global, this gets rid of old handlers
            handlers = logger.handlers[:]
            for handler in handlers:
                handler.close()
                logger.removeHandler(handler)
            
            handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=100000000, backupCount=20)
            handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
            logger.addHandler(handler)
            
            self.logger = logger
            
    # %%

    if __name__ == '__main__':
        
        log = LogClass()

        log.logger.info('test2')