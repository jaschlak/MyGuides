# Logging

    Code for logging
    
## Rolling Logs based on file size

    import logging
    from logging import handlers

    class LogClass:
        
    def __init__(self, logname='test'):
        
        if os.name == 'nt':
            folderpath = 'C:\Logs'
            filename = logname + '.log'
        elif os.name == 'posix':
            folderpath = './logs'
            filename = logname + '.log'
        else:
            folderpath = '~'
            filename = 'couldnt_detect_os.log'
            
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
            
    # %%

    if __name__ == '__main__':
        
        log = LogClass()

        log.logger.info('test2')