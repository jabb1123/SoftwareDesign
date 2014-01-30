# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:13:21 2014

@author: jacob
"""

def grid():
    for i in range(11):
        if i==0 or i==5 or i==10:
            print '+----+----+'
        else:
            print '|    |    |'