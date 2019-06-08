from tkinter import *

root=Tk()
canvas=Canvas(width=400,height=450)
canvas.pack()
photo=PhotoImage(file='//home//kuma-company//tkinter_learn//modi.png')
canvas.create_image(0,0,image=photo,anchor=NW)

root.geometry("600x600+120+120")
root.mainloop()
