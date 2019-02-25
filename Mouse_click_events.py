from tkinter import *

root=Tk()
def rclick(event):
	print("U r click Right Button")
def mclick(event):
	print(" U r click Middle Button")
def lclick(event):
	print("U r click Left Button")

frame=Frame(root,width=500,height=500)
frame.bind("<Button-1>",rclick)
frame.bind("<Button-2>",mclick)
frame.bind("<Button-3>",lclick)
frame.pack()
root.mainloop()
