# -*- coding: utf-8 -*-

''' 
killswitch.txt file will be created
add anything to it to stop logging to C:\Logs\python_service.log
'''
   


import time
from support.log import LogClass
import datetime
import os

filename = 'killnow.txt'

def create_file():

    if not os.path.exists(filename):
        file=open(filename,"w")
        file.close()
        
def read_and_kill():
    
    create_file()
    
    try:
        file = open(filename,"r")
        txt_cont=file.read()
        file.close()
        
        if len(txt_cont) == 0 or '0' in txt_cont:
            return False
        else:
            return True
    except Exception as e:
        print("couldn't access file")
        return False

def write_to_logs_unless_killed():

    Log = LogClass()
    
    last_time = time.time()

    Log.logger.info('Starting Service at: {}'.format(datetime.datetime.now()))

    while True:
        
        if read_and_kill():
            break
        
        if time.time() - last_time > 5:
            
            Log.logger.info('last_update: {}'.format(datetime.datetime.now()))
            last_time = time.time()
            
    
            
            
if __name__ == '__main__':
    
    write_to_logs_unless_killed()