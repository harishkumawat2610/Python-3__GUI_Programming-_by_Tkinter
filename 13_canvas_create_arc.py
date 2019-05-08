from tkinter import *
root=Tk()

canvas=Canvas(root,width=250,height=250,bg='red')
canvas.pack()
#Defualt extent(angle) is 90
canvas.create_arc(10,10,220,220,fill='yellow')

canvas=Canvas(root,width=250,height=250,bg='red')
canvas.pack(side=BOTTOM)
#change extent(angle)
canvas.create_arc(10,10,220,220,fill='yellow',extent=130)

root.geometry("600x600+120+120")
root.mainloop()

