from tkinter import *
from tkinter import colorchooser
def choose():
	clr=colorchooser.askcolor(title="Choose Color")
	root.configure(background=clr[1])
root=Tk()
bt=Button(root,text="Change Color", command=choose)
bt.pack()

root.geometry("400x400+150+150")
root.mainloop()
