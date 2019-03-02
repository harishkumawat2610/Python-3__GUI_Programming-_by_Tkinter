from tkinter import *
from tkinter import messagebox

def call_me():
	answer=messagebox.askyesnocancel("exit","Do you sure to exit")
	print(answer)

root=Tk()
b1=Button(root,text="Exit",command=call_me)
b1.pack()

root.geometry("400x300+150+150")
root.mainloop()
