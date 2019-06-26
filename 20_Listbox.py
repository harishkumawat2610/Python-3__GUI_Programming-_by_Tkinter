from tkinter import *

root=Tk()
#selectmode=MULTIPLE/SINGLE/EXTENDED
lb=Listbox(root,width=30,height=20,selectmode=EXTENDED)
lb.insert(1,"java")
lb.insert(2,"C")
lb.insert(3,"C++")
lb.insert(4,"Python")
lb.insert(5,"HTML")
lb.insert(6,"Css")
lb.insert(7,"JavaScript")
lb.pack()
root.geometry("400x400+150+150")
root.mainloop()
