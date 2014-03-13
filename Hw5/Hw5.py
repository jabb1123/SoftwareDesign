# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:15:27 2014

@author: jacob
"""

import re

def load_book(text):  
#This function loads the book from a .txt file. It also cuts off the beginning and end tag.
    f=open(text,'r')
    book=f.read()
    f.close()
    startOfBook=book.index(' ***')+4
    book=book[startOfBook:]
    endOfBook=book.index('End of the Project')
    book=book[:endOfBook]
    return book

def get_words_from_book(text):
#Creates a list of all the words the from the string.
    return re.findall("[a-zA-Z']+",text)
    
def parse_through_text(textList):
    # I commend you for using map function, but why not use map on a list of all words you want replaced to do what you're doing?
    newText=map(lambda x: str.replace(x,'the',''),textList)
    newText=map(lambda x: str.replace(x,'The',''),newText)
    newText=map(lambda x: str.replace(x,'for',''),newText)
    newText=map(lambda x: str.replace(x,'with',''),newText)
    newText=map(lambda x: str.replace(x,'from',''),newText)
    newText=map(lambda x: str.replace(x,'because',''),newText)
    newText=map(lambda x: str.replace(x,'about',''),newText)
    newText=map(lambda x: str.replace(x,'through',''),newText)
    newText=map(lambda x: str.replace(x,'after',''),newText)
    newText=map(lambda x: str.replace(x,'over',''),newText)
    newText=map(lambda x: str.replace(x,'between',''),newText)
    newText=map(lambda x: str.replace(x,'out',''),newText)
            
    return newText
    
def Compare_number_of_occurances(word1,word2,textList):
    #Takes an input for two words and a list of words.  Returns the count of the words.
    x=0
    y=0
    for i in range(len(textList)):
        if textList[i]==word1:
            x+=1
        elif textList[i]==word2:
            y+=1
    return (x,y)
    # I don't understand what the purpose of this function is..?

    '''  
def Analyze_bible(word1,word2):
    bible=load_book('Bible.txt')
    wordList=parse_through_text(bible)
    (x,y)=Compare_number_of_occurances(word1,word2,wordList)
    if x>y:
        print 'There were '+str(x)+' occurances of the word '+word1 +' and '+str(y)+' occurances of '+word2
    else:
         print 'There were '+str(y)+' occurances of the word '+word2+' and '+str(x)+' occurances of '+word1
    '''