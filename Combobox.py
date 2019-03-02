from tkinter import *
from tkinter.ttk import Combobox
def click_me():
	hk=combo.get()
	mk=combo1.get()
	print(hk,mk)
root=Tk()
list_items=["C","C++","Python","java","HTML","CSS"]
l=list(range(1,32))
combo=Combobox(root,value=list_items)
combo.set("C")
combo.pack()
combo1=Combobox(root,value=l)
combo1.set("1")
combo1.pack()
print(combo)
bt1=Button(root,text="Submit",command=click_me)
bt1.pack()
root.geometry("200x200+150+150")
root.mainloop()
