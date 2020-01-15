from tkinter import *

root = Tk()
root.geometry("400x400")

lbox = Listbox(root)

lbox.insert(1,'English')
lbox.insert(2,'Marathi')
lbox.insert(3,'hindi')
lbox.insert(4,'others')
lbox.place(x=100,y=100)

root.mainloop()