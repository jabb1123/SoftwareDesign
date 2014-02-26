# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 13:40:45 2014

@author: jacob
"""
List=[]
def recursive_flatten(myList):
    List=[]
    for i in range (len(myList)):
        if type(myList[i]) is list:
            List=List+recursive_flatten(myList[i])
        else:
            List.append(myList[i])
    return List