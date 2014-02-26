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
    textList = [x for x in textList if x != 'a' or 'the' or 'an' or 'to'or 'of' or 'in' or 'for' or 'at' or 'with' or 'on' or'from' or'by' or 'about' or 'as' or 'through' or 'after' or 'over' or 'between' or 'out' or 'because']
    return textList