# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:50:13 2020

@author: jschlak
"""
import re

# gets a count of substrings within main string
def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)):
        if re.search('^'+sub_string+'.*',string[i:]):
            count += 1
    return count

string = 'ABCDCDC'
sub_string = 'CDC'
        
count = count_substring(string, sub_string)

print(count)