import random
import string
from tkinter import *

#alphabet
alphabet = list(string.ascii_lowercase)

#create list of words from dictionary
with open("58110.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

#divide list of words
dct = {}
for element in lines:
    if len(element) not in dct:
        dct[len(element)] = [element]
    elif len(element) in dct:
        dct[len(element)] += [element] 
res = []
for key in sorted(dct):
    res.append(dct[key])

#decoding function
def decode():
  #receive input and divide string into list
  originaltext=str(textentry.get())
  originaltext=originaltext.split(" ")
  finaltext=""
  e=1
  for word in originaltext:
    wordlength=len(word)
    possiblewords=[]
    #range of numbers to try
    for i in range(0, 27):
      newword=""
      for letter in word:
        #is letter in the lowercase alphabet?
        if letter in alphabet:
          position=alphabet.index(letter)
          newposition=position+i
          if newposition>25:
            newposition%=26
          elif newposition<0:
            newposition+=26
          newword+=alphabet[newposition]
        #is letter in the uppercase alphabet?
        elif letter.isupper()==True:
          lower=letter.lower()
          position=alphabet.index(lower)
          newposition=position+int(i)
          if newposition>25:
            newposition%=26
          elif newposition<0:
            newposition+=26
          newword+=alphabet[newposition].upper()
        #rest of the characters are not changed
        else:
          newword+=letter
      #compares new word with every word with the same length
      for w in dct[wordlength]:
        if newword.lower()==w.lower():
          possiblewords.append(newword)
          continue
    #displays different options when there are more than two "matches"
    if len(possiblewords)==1:
      finaltext+=possiblewords[0]
      finaltext+=" "
    else:
      finaltext+="[{}]".format(e)
      clicked = StringVar()
      clicked.set("[{}]".format(e))
      drop=OptionMenu(root, clicked, *possiblewords)
      drop.pack(padx=5, side=LEFT)
      finaltext+=" "
      e+=1
  Frame2 = Frame(root,bg="SteelBlue3")
  Frame2.place(relx=0.13,rely=0.9, relwidth=0.7,relheight=0.3)
  label2 = Label(Frame1,text=finaltext,bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
  label2.place(relx=0.05,rely=0.9, relheight=0.08)

#encoding function
def encode():
  #receive input and divide string into list
  originaltext=str(textentry.get())
  originaltext=originaltext.split(" ")
  finaltext=""
  for word in originaltext:
    #generates a random shiftnumber
    shiftnumber=random.randint(1, 20)
    for letter in word:
      #is letter in the lowercase alphabet?
      if letter in alphabet:
        position=alphabet.index(letter)
        newposition=position+int(shiftnumber)
        if newposition>25:
          newposition%=26
        finaltext+=alphabet[newposition]
      #is letter in the uppercase alphabet?
      elif letter.isupper()==True:
        lower=letter.lower()
        position=alphabet.index(lower)
        newposition=position+int(shiftnumber)
        if newposition>25:
          newposition%=26
        finaltext+=alphabet[newposition].upper()
      #rest of the characters are not changed
      else:
        finaltext+=letter
    finaltext+=" "
  #copy output to clipboard
  root.clipboard_append(finaltext.rstrip())
  Frame2 = Frame(root,bg="SteelBlue3")
  Frame2.place(relx=0.13,rely=0.7, relwidth=0.7,relheight=0.3)
  label2 = Label(Frame1,text=finaltext,bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
  label2.place(relx=0.05,rely=0.7, relheight=0.08)

#main GUI
root = Tk()
root.geometry('700x700')
root.title("Cipher System")
root.config(bg='SteelBlue3')

#header
headingFrame = Frame(root,bg="azure",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Welcome to the Cipher System", bg='azure', font=('Helvetica',20,'bold'))
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
