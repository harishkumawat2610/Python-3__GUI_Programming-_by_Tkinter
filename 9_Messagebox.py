from tkinter import *
from tkinter import messagebox
def sinfo():
	messagebox.showinfo("Success","Understand")
def einfo():
	messagebox.showerror("Error","Understand")
def winfo():
	messagebox.showwarning("Waring ","Understand")

root=Tk()
b1=Button(root,text="ShowInfo button",command=sinfo)
b2=Button(root,text="ShowError button",command=einfo)
b3=Button(root,text="ShowWarring button",command=winfo)
b1.pack()
b2.pack()
b3.pack()
root.geometry("400x400+150+150")
root.mainloop()

