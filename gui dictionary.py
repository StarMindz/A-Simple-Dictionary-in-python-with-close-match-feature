# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:47:37 2020

@author: USER
"""

from tkinter import *
import json
from difflib import get_close_matches

root=Tk()
root.title("My Smart Dictionary-- A Work of StarMinds")
root.geometry("500x500")

global entry
request=StringVar()
word=StringVar()
meaning=StringVar()
word.set("Enter your Word")
meaning.set("")
data = json.load(open("data.json"))


def backend():
    global entry 
    global meaning
    global word
    global data
    meaning.set("")
    try:
        word.set("\nEnter your word:")
        worde=entry.get()
        if worde in data.keys():
            word1=worde
        elif worde.capitalize() in data.keys():
            word1=worde.capitalize()
        elif worde.lower() in data.keys():
            word1=worde.lower()
        elif worde.upper() in data.keys():
            word1=worde.upper()
        else:
            word1=get_close_matches(worde,data.keys(),1)
            meaning.set("\n\nSorry the word \"{}\" doesn't exist. I searched for \"{}\" instead\n\n".format(worde,word1[0]))
            word1=word1[0]
        meanings=data[word1]
        wordcap=(word1.capitalize()+" means: "+ "\n")
        meaning.set(meaning.get()+wordcap)
        count=1
        translate=""
        for means in meanings:
            translate+=("\n"+str(count)+" "+means+"\n")
            count+=1
        meaning.set(meaning.get()+translate)
            
        
    except:
        word.set("\nThis word doesn't exist. Please try inputting a correct English word")


def frontend():
    global word
    global meaning
    global entry
    frame=Frame(root,width=300,height=400,bg="Pink")
    frame.pack()
    label=Label(frame,text="Welcome! This is a simple dictionary created by StarMinds", padx=400, background="pink", font="Arial  13")
    label.pack(side="top")
    label1=Label(root, textvariable=word, font="Arial 11")
    label1.pack()
    entry=Entry(root)
    entry.pack()
    frame1=Frame(root, relief="sunken")
    frame1.pack()
    label2=Label(frame1,textvariable=meaning,font="Arial 12")
    button=Button(frame1,text="Search", command=backend)
    button.pack()
    label2.pack()



frontend()

mainloop()
