# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 23:29:18 2020

@author: USER
"""
from difflib import get_close_matches
import json

data = json.load(open("data.json"))
while True:
    try:
        word=input("\nEnter your word:")
        if word in data.keys():
            word1=word
        elif word.capitalize() in data.keys():
            word1=word.capitalize()
        elif word.lower() in data.keys():
            word1=word.lower()
        elif word.upper() in data.keys():
            word1=word.upper()
        else:
            word1=get_close_matches(word,data.keys(),1)
            print("\n\nSorry the word {} doesn't exist. I searched for {} instead\n\n".format(word,word1[0]))
            word1=word1[0]
        meaning=data[word1]
        print(word1.capitalize()+" means: "+ "\n")
        count=1
        for means in meaning:
            print(str(count)+" "+means)
            count+=1
            
        
    except:
        print("\nThis word doesn't exist. Please try inputting a correct English word")