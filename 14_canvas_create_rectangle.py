from tkinter import *
root=Tk()
canvas=Canvas(width=400,height=400 ,bg='yellow')
canvas.pack()
canvas.create_rectangle(100,100,300,250,fill="red",outline='yellow')
root.mainloop()
