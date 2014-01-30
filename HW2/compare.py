# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:40:10 2014

@author: jacob
"""

def compare():
    x = raw_input('What is the value of x?\n')
    x = int(x)
    y = raw_input('What is the value of y?\n')
    y = int(y)
    if x>y:
        return 1
    if x==y:
        return 0
    else:
        return -1