# Logging

    Code for logging
    
## Rolling Logs based on file size

    import logging
    from logging import handlers

class LogClass:
    
    def __init__(self):
        
        self.logger = logging.getLogger()
        self.level = logging.DEBUG
        
        if os.name == 'nt':
            folderpath = 'C:\Logs'
            filename = <logname> + '.log'
        elif os.name == 'posix':
            folderpath = './logs'
            filename = <logname> + '.log'
        else:
            folderpath = '~'
            filename = 'couldnt_detect_os.log'
            
        LOGFILEPATH = '/'.join([folderpath,filename])
        
        if not os.path.exists(folderpath):
            os.makedirs(folderpath)
        
        
        self.set_log_settings()
        self.set_log_directory(LOGFILEPATH)
        
        
    def set_log_settings(self):
        
        self.logger.setLevel(self.level)
        
    def set_log_directory(self, LOGFILEPATH):
        
        # important, handlers are global, this gets rid of old handlers
        handlers = self.logger.handlers[:]
        for handler in handlers:
            handler.close()
            self.logger.removeHandler(handler)
        
        handler = logging.handlers.RotatingFileHandler(LOGFILEPATH, maxBytes=100000000, backupCount=20)
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        self.logger.addHandler(handler)


    if __name__ == '__main__':
        
        log = LogClass()

        log.logger.info('test2')
        log.set_log_directory('C:\Logs\IJustWantedToShowICanChange.log')
        log.level = logging.INFO
        log.set_log_settings()