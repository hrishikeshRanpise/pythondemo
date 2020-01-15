from tkinter import *
from tkinter import messagebox
import sqlite3

login = Tk()
login.title("Login Page")
login.geometry("300x300")

def auth():
	login.destroy()
	dashboard = Tk()
	dashboard.title("Dashboard")
	dashboard.geometry("1200x800")

	labname = Label(dashboard,text="Name").place(x=40,y=40)
	#labnqual = Label(dashboard,text="Qualification").place(x=40,y=180)
	#labspc = Label(dashboard,text="Specialisation").place(x=40,y=120)
	global dname
	#global dqual
	#global dspc
	dname =StringVar()
	ent1 = Entry(dashboard,variable=dname)
	
	btnsub = Button()

	dashboard.mainloop()

btn= Button(login,text="Login",command=auth)
btn.pack()


login.mainloop()