from tkinter import *
#Create Window
root=Tk()

#Create Name and Password label
name=Label(root,text="Name")
password=Label(root,text="Password")

#Create Entry boxes for name and password
nentry=Entry(root)
pentry=Entry(root)

#set name and name-entry according to grid
name.grid(row=0,sticky=E)
nentry.grid(row=0,column=1)

#set password and password-entry according to grid
password.grid(row=1,column=0)
pentry.grid(row=1,column=1)

#Create Check box for Check Mark
check=Checkbutton(root,text="Remenber Me")
check.grid(columnspan=2)

root.mainloop()
