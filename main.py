from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x400")
ttk.Button(root, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
