from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Login form")
root.geometry("400x400")
l1=Label(root,text="Username")
l1.place(x=20,y=10)

def clr():
	ent1.delete(0,END)
	ent2.delete(0,END)

ent1=Entry(root)
ent1.place(x=100,y=10)
"""
def login():
	print(ent1.get())
	print(ent2.get())
"""	

def login():
	if ent1.get()=="Rushi" and ent2.get()=="1234" :
		print("Login Successful")
		#msg=messagebox.showinfo("Login Status","Login Successful")
		msg=messagebox.showerror("Error","No such item found")
	else:
		print("Login Failed")
		#msg=messagebox.showinfo("Login Status","Login Failed")
		msg=messagebox.showerror("Error","No such item found")



l2=Label(root,text="Password")
l2.place(x=20,y=40)

ent2=Entry(root,show="*")
ent2.place(x=100,y=40)

b1=Button(root,text="Login",command=login)
b1.place(x=100,y=70)

b2=Button(root,text="Clear",command=clr)
b2.place(x=150,y=70)


root.mainloop()
