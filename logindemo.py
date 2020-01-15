from tkinter  import *
from tkinter import messagebox

root = Tk()
root.title("Entry Demo")
root.geometry("400x300")

lbl1 = Label(root,text="Name").place(x=40,y=40)

lbl2 = Label(root,text="Password").place(x=40,y=80)

ent1 = Entry(root,)
ent1.place(x= 100,y=40)

ent2 = Entry(root,show="*")
ent2.place(x= 100,y=80)

def disp():
	if ent1.get() == "hrishikesh" and ent2.get() == "password":
		print("login successful")
		msg = messagebox.showinfo("title","Login successful")
	else:
		msg = messagebox.showinfo("")


def clr():
	ent1.delete(0,END)
	ent2.delete(0,END)

btn1 = Button(root, text="Display name", command=disp)
btn1.place(x= 70,y=140)
btn2 = Button(root, text="Clear Fields", command=clr)
btn2.place(x= 160,y=140)


root.mainloop()