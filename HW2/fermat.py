# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:18:17 2014

@author: jacob
"""

def fermat_input():
    a = raw_input ('What is the value of a?\n')
    a=int(a)
    b = raw_input ('What is the value of b?\n')
    b=int(b)
    c = raw_input ('What is the value of c?\n')
    c=int(c)
    n = raw_input ('What is the value of n?\n')
    n=int(n)
    check_fermat(a,b,c,n)

def check_fermat(a,b,c,n):
    if a**n+b**n==c**n:
        print 'Holy smaokes, Fermat was wrong!'
    else:
        print 'No, that doesn\'t work'

            
