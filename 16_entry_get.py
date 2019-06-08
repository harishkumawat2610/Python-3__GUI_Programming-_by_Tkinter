from tkinter import *

def click_me():
	s=entry1.get()
	if s=='harish':
		print("success")
	else:
		print('fail')

root=Tk()
entry1=Entry(root)
entry1.pack()
bt1=Button(root,text="Submit",command=click_me).pack()
root.geometry("400x400+150+150")
root.mainloop()
