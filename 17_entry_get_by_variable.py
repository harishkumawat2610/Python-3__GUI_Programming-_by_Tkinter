from tkinter import *

def click_me():
	hk=h.get()
	print(hk)
	if hk=='admin':
		print("done")
	else:
		print("fail")


root=Tk()
h=StringVar()
entry1=Entry(root,textvariable=h).pack()
h.set("harish")

bt1=Button(root,text="Done",command=click_me).pack()
root.geometry("400x400+150+150")
root.mainloop()
