from tkinter import *

root=Tk()

#create canvas with height 250 and width 250
canvas=Canvas(root,width=250,height=250,bg='yellow')
canvas.pack()
#create red line from (250,0) to (0,100)
red_line=canvas.create_line(250,0,0,100,fill='red')
blue_line=canvas.create_line(0,100,250,250,fill='blue')
root.geometry("400x400+150+150")
root.mainloop()
