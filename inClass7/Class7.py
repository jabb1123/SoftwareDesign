# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:44:14 2014

@author: jacob
"""

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
    
def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)