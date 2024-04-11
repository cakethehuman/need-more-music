from tkinter import *
import webbrowser
from tkinter import ttk


def start_music():
    webbrowser.open("https://www.youtube.com/watch?v=E5Jy_h1eHzY&list=RDAqI97zHMoQw&index=2")
    # select music

def party_music():
    webbrowser.open("https://www.youtube.com/watch?v=E5Jy_h1eHzY&list=RDAqI97zHMoQw&index=2")

def quit_application():
    root.destroy()

root = Tk()
root.geometry("600x400")

# Create and place the label 
label = ttk.Label(root, text="hewo im emu")
label.grid(column=5, row=0)

button = ttk.Button(root, text="music", command=start_music)
button.grid(column=5, row=1)

button = ttk.Button(root, text="black people music", command=start_music)
button.grid(column=5, row=1)

# Create and place the button 
button = ttk.Button(root, text="Quit", command=quit_application)
button.grid(column=5, row=2)

root.mainloop()
