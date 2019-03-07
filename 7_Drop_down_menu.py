from tkinter import * 
root= Tk()

def openfile():
	print("today not open this file:")

main_menu=Menu(root)
root.config(menu=main_menu)
#Create file Menu
fileMenu=Menu(main_menu)
main_menu.add_cascade(label="file",menu=fileMenu)
fileMenu.add_command(label="open",command=openfile)
fileMenu.add_separator()
fileMenu.add_command(label="New File",command=openfile)
fileMenu.add_separator()
fileMenu.add_command(label="Save",command=openfile)
#create edit menu
editMenu=Menu(main_menu)
main_menu.add_cascade(label='Edit',menu=editMenu)
root.mainloop()
