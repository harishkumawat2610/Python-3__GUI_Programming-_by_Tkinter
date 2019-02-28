from tkinter import *

root=Tk()
def Bclick(event):
	print("Click Button Calling by binding")

button1=Button(root,text="Click")
button1.bind("<Button-1>",Bclick)
button1.pack()
root.mainloop()
