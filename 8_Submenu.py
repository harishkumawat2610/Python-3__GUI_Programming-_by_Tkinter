from tkinter import *

root=Tk()
def openfile():
	print("Hello friends")

main_menu=Menu(root)
root.config(menu=main_menu)

fileMenu=Menu(main_menu)
main_menu.add_cascade(label="file",menu=fileMenu)
fileMenu.add_command(label="open",command=openfile)
fileMenu.add_separator()
fileMenu.add_command(label="New file",command=openfile)
fileMenu.add_separator()

Newfile=Menu(fileMenu)
Newfile.add_command(label="Tools",command=openfile)
Newfile.add_command(label="Setting",command=openfile)
fileMenu.add_cascade(label="option",menu=Newfile)
root.mainloop()

