from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("200x200")

rb = StringVar()

lbl1 = Label(root).pack()

def select():
	str1 = "you selected "+rb.get()

Radiobutton(root,text="Male",variable=rb,value="male",command=select).pack()
Radiobutton(root,text="Female",variable=rb,value="female",command=select).pack()


root.mainloop()
