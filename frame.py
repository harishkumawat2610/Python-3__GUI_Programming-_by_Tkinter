from tkinter import *
root =Tk()

frame= Frame(root)
name=Label(root,text='name')
password=Label(root,text='password')
entry1=Entry(root)
entry2=Entry(root)
name.grid(row=0,sticky=E)
entry1.grid(row=0,column=1)
password.grid(row=1)
entry2.grid(row=1,column=1)
root.mainloop()
