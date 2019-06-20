from tkinter import *
def click_me():
	print(h.get())
root=Tk()
h=StringVar()
check_bt=Checkbutton(root,text="item1",variable=h, offvalue="uncheck",onvalue="check'").pack()
bt1=Button(root,text='submit',command=click_me).pack()
root.geometry("500x500+150+150")
root.mainloop()
