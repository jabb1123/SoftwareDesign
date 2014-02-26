# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:15:27 2014

@author: jacob
"""

import re

def load_book(text):
    f=open(text,'r')
    book=f.read()
    f.close()
    startOfBook=book.index(' ***')+4
    book=book[startOfBook:]
    endOfBook=book.index('End of the Project')
    book=book[:endOfBook]
    return book
    
def get_words_from_book(text):
    return re.findall("[a-zA-Z']+",text)
    
def parse_through_text(textList):
    i=0
    while i>len(textList):
        try:
            textList.remove('a')
            textList.remove('the')
            textList.remove('an')
            textList.remove('to')
            textList.remove('of')
            textList.remove('in')
            textList.remove('for')
            textList.remove('at')
            textList.remove('with')
            textList.remove('on')
            textList.remove('from')
            textList.remove('by')
            textList.remove('about')
            textList.remove('as')
            textList.remove('through')
            textList.remove('after')
            textList.remove('over')
            textList.remove('between')
            textList.remove('out')
            textList.remove('because')
            
            
        except:
            pass
        i+=1
    return textList