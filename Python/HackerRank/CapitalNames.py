# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:35:32 2020

@author: jschlak
"""

import re

def cap_names(string):
    
    cap_name_string = ''
    capnext = False
    
    for i,item in enumerate(string):
        #print('Intermediate:\n' + cap_name_string + '\n' + str(capnext) + '\n\n')
        #print('Intermediate:\n' + cap_name_string +'\n\n')
        
        # if alpha
        if re.search('[a-zA-Z]', string):
            
            # if beginning, capitalize it
            if i == 0:
                cap_name_string += string[0].upper()
                
            # if space, note the next letter needs to be cap
            elif item == ' ':
                capnext = True
                cap_name_string += string[i]
                
            # if tagged for cap, cap it and remove tag
            elif capnext == True:
                cap_name_string += string[i].upper()
                capnext = False
            
            # else, leave it lowercase
            else:
                cap_name_string += string[i].lower()
            
        # if not letter, leave it alone and pass it
        else:
            cap_name_string += string[i]
    
    return cap_name_string

string = 'hello   world  lol'

print(cap_names(string))