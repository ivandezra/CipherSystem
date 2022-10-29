from tkinter import *
from tkinter import messagebox
import random

#alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open("58110") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

#decoding function
def decode():
  originaltext=str(textentry.get())
  originaltext=originaltext.split(" ")
  finaltext=""
  for word in originaltext:
    for i in range(0, 20):
      newword=""
      for letter in word:
        if letter in alphabet:
          position=alphabet.index(letter)
          newposition=position+i
          if newposition>25:
            newposition%=26
          elif newposition<0:
            newposition+=26
          newword+=alphabet[newposition]
        elif letter.isupper()==True:
          lower=letter.lower()
          position=alphabet.index(lower)
          newposition=position+int(i)
          if newposition>25:
            newposition%=26
          elif newposition<0:
            newposition+=26
          newword+=alphabet[newposition].upper()
        else:
          newword+=letter
      for w in lines:
        if newword.lower()==w and len(newword)==len(w):
          finaltext+=newword
    finaltext+=" "
  Frame2 = Frame(root,bg="SteelBlue3")
  Frame2.place(relx=0.13,rely=0.9, relwidth=0.7,relheight=0.3)
  label2 = Label(Frame1,text=finaltext,bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
  label2.place(relx=0.05,rely=0.9, relheight=0.08)

#encoding function
def encode():
  originaltext=str(textentry.get())
  originaltext=originaltext.split(" ")
  finaltext=""
  for word in originaltext:
    shiftnumber=random.randint(0, 20)
    for letter in word:
      if letter in alphabet:
        position=alphabet.index(letter)
        newposition=position+int(shiftnumber)
        if newposition>25:
          newposition%=26
        finaltext+=alphabet[newposition]
      elif letter.isupper()==True:
        lower=letter.lower()
        position=alphabet.index(lower)
        newposition=position+int(shiftnumber)
        if newposition>25:
          newposition%=26
        finaltext+=alphabet[newposition].upper()
      else:
        finaltext+=letter
    finaltext+=" "
  Frame2 = Frame(root,bg="SteelBlue3")
  Frame2.place(relx=0.13,rely=0.7, relwidth=0.7,relheight=0.3)
  label2 = Label(Frame1,text=finaltext,bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
  label2.place(relx=0.05,rely=0.7, relheight=0.08)

#main GUI
root = Tk()
root.geometry('700x700')
root.title("Encryption System")
root.config(bg='SteelBlue3')

#header
headingFrame = Frame(root,bg="azure",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Welcome to the Encryption System", bg='azure', font=('Helvetica',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#text input
Frame1 = Frame(root,bg="SteelBlue3")
Frame1.place(relx=0.13,rely=0.15, relwidth=0.7,relheight=0.3)

label1 = Label(Frame1,text="Enter the text: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.08)

textentry = Entry(Frame1,font=('Century 12'))
textentry.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#encode button
button1 = Button(root, text='Encode',font=('Courier',15,'normal'),command=encode)
button1.place(relx=0.25,rely=0.6, relwidth=0.25, relheight=0.05)

#decode button
button2 = Button(root, text='Decode',font=('Courier',15,'normal'),command=decode)
button2.place(relx=0.5,rely=0.6, relwidth=0.25, relheight=0.05)

root.mainloop()
