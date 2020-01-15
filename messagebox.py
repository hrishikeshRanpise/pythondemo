from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")

def hello():
	msg = messagebox.showinfo("title","you clicked the button")

btn = Button(root,text="Click me",bd=5, command=hello)

def warn():
	warnmsg = messagebox.showwarning("title","warning!")

btn1 = Button(root,text="warning",bd=5, command=warn)

def yesno():
	ynmsg = messagebox.askyesno("title","yes or no?")


btn2 = Button(root,text="Yes No",bd=5,command=yesno)

def err():
	errmsg = messagebox.showerror("title","there is an error")

btn3 = Button(root,text="error",bd=5,command=err).pack()

btn.pack()
btn1.pack()
btn2.pack()

root.mainloop()