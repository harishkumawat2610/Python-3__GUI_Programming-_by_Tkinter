from tkinter import *
root=Tk()
#vertical slider
s=Scale(root,from_=0,to=100)
s.pack(side=LEFT,fill=Y)
root.geometry('200x200')
root.mainloop()
