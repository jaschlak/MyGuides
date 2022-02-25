# -*- coding: utf-8 -*-

from celery import Celery

''' run

navigate to folder
celery worker -A tasks --pool=solo --loglevel=info

ipython
from tasks import fav_doctor
fav_doctor.delay()
dir(fav_doctor)

'''

app = Celery()
app.config_from_object('celeryconfig')

suf = lambda n: "%d%s" % (n, {1: "st", 2: "nd", 3: "rd"}.get(n if n < 20 else n % 10, "th"))

@app.task
def fav_doctor():
    """Reads doctor.txt file and prints out fav doctor, then adds a new
    number to the file"""
    
    with open('doctor.txt', 'r+') as f:
        for line in f:
            nums = line.rstrip().split()
            
            print('The {} doctor is my favorite'.format(suf(int(nums[0]))))
            
            for num in nums[1:]:
                print('Wait! The {} doctor is my favorite'.format(suf(int(num))))
                
            last_num = int(nums[-1])
            new_last_num = last_num + 1
            
            f.write(str(new_last_num) + ' ')
            
    return 'doctor {} is the best!!!'.format(num)