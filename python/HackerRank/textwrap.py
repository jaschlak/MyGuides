# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:44:15 2020

@author: joebl
"""


def wrap(string, max_width):
    newstring = ''
    eq = len(string) / max_width
    mylen = int(eq)
    
    for i in range(mylen):
        newstring += string[i*max_width:i*max_width+max_width] + '\n'
        
    if len(string) % max_width != 0:
        newstring += string[(i+1)*max_width:]
    else:
        newstring = newstring[:-2]
        
    return newstring


string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
(max_width) = 4

print(wrap(string, max_width))


#print(mylen)