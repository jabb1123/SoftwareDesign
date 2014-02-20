# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:42:06 2014

@author: jacob
"""

def sum_of_squares(num):
    Sum=0
    for x in range (num):
        Sum+=(x+1)**2
    return Sum

def filter_out_negative_numbers(listin):
    x=0    
    while x<len(listin):
        if listin[x]<0:
            del listin[x]
        x+=1
    return listin