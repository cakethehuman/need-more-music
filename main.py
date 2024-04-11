from tkinter import *
import webbrowser
from tkinter import ttk
import random


def anime():
    return #your link

def party():
    return #your link

def start_music(url):
    webbrowser.open(url)

def quit_application():
    root.destroy()

root = Tk()

# Create and place the label 
label = ttk.Label(root, text="hewo im emu")
label.grid(column=5, row=0)

# Create and place the button 
button1 = ttk.Button(root, text="anime music", command=lambda: start_music(anime()))
button1.grid(column=5, row=1)

# Create and place the button 
button2 = ttk.Button(root, text="party music", command=lambda: start_music(party()))
button2.grid(column=5, row=2)

# Create and place the button 
button3 = ttk.Button(root, text="Quit", command=quit_application)
button3.grid(column=5, row=5)

root.mainloop()

