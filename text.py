import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
text_speech=pyttsx3.init()
box=Tk()
box.title("Text to Speech converter")
box.configure(bg="#305065")
box.geometry("900x450+200+200")
box.resizable(False,False)

engine=pyttsx3.init()
def speaknow():
    text=textarea.get(1.0,END)
    gender=genderbox.get()
    speed=speedbox.get()
    voices=engine.getProperty('voices')
    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Noraml'):
            engine.setProperty('rate',220)
            setvoice()
        else:
            engine.setProperty('rate',150)
            setvoice()
def download():
    print()

imageicon=PhotoImage(file="speak.png")
box.iconphoto(False,imageicon)

topframe=Frame(bg="white",width=900,height=100)
topframe.place(x=0,y=0)

logo=PhotoImage(file="speakerlogo.png")
Label(topframe,image=logo,bg="white").place(x=10,y=5)

Label(topframe,text="Text to Speech",font="arial 20 bold",bg="white",fg="black").place(x=50,y=30)
textarea=Text(font="Robote 20",bg="white",relief=GROOVE, wrap=WORD)
textarea.place(x=10,y=150,width=500,height=250)

Label(text="Voice",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(text="Speed",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)

genderbox=Combobox(values=['Male','Female'],font="arial 14",state='r',width=10)
genderbox.place(x=550,y=200)
genderbox.set('Male')

speedbox=Combobox(values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speedbox.place(x=730,y=200)
speedbox.set('Normal')

# imageicon=PhotoImage(file="speak.png")
btn=Button(text="Speak",compound=LEFT,width=10,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)

btn=Button(text="Save",compound=LEFT,width=10,font="arial 14 bold",command=download)
btn.place(x=730,y=280)
box.mainloop()