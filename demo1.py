from tkinter import *

root = Tk()
root.title("demo1")

root.geometry("400x300")


def display():
	demo = e.get()
	lbl = Label(root, text=demo).place(x=100,y=190)


e = Entry(root)
e.place(x=100,y=100)


btn = Button(root,text="click", command=display).place(x=100,y=150)


root.mainloop()

