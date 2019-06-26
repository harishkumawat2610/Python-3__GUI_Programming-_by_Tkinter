from tkinter import *
def click_me():
	hk=h.get()
	if hk==1:
		print("male")
	else:
		print("female")
root=Tk()
h=IntVar()
bt1=Radiobutton(root,text="male",value=1,variable=h).pack()
bt2=Radiobutton(root,text="female",value=2,variable=h).pack()
bt3=Button(root,text="Submit",command=click_me).pack()
root.geometry("500x500+150+150")
root.mainloop()
