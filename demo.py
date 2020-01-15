from tkinter import *
import tkinter.messagebox
import sqlite3

login = Tk()

login.title("login Page");
login.geometry("400x300");

global usern , passwd

def logindemo():
	username = usern.get()
	password = passwd.get()

	if username=="hrishikesh" and password=="password":
		anotherw()

	else:
		fail = Label(login,text="login failed").place(x=150,y=175)

def anotherw():
	t = tkinter.messagebox.showinfo("Login Successful","Login Successful")
	login.destroy()+
	newroot = Tk()
	newroot.geometry("800x800")
	newroot.title("Admin Panel")

	head = Label(newroot,text="Add Doctor").place(x=350,y=50)

	def addDoctor():
		docname =dentry.get()
		quali = dqentry.get()
		conn = sqlite3.connect("new.db")
		with conn:
			cur = conn.cursor()
			cur.execute('INSERT INTO doctor(name,quali) VALUES(?,?)',(docname,quali))
		dentry.delete(0, END)
		dqentry.delete(0, END)
		success = tkinter.messagebox.showinfo("Record Inserted","Record Inserted Successful")

	def display():
		newroot.destroy()
		showdoc = Tk()
		showdoc.title("All Doctors")
		showdoc.geometry("600x600")
		

	dname = Label(newroot,text="Doctor Name").place(x=100,y=100)
	dqual = Label(newroot,text="Qualification").place(x=100,y=130)
	dentry = Entry(newroot)
	dentry.place(x=200,y=100)
	dqentry = Entry(newroot)
	dqentry.place(x=200,y=130)
	addDoc = Button(newroot, text="Add", command=addDoctor).place(x=130,y=160)
	showall = Button(newroot, text="Show All", command=display).place(x=180,y=160)


	newroot.mainloop()

def cancel():
	login.quit()


label1 = Label(login,text="Username").place(x=100,y=50)
usern = Entry(login,width=20,bd=5)
usern.place(x=170,y=50)
label2 = Label(text="Password").place(x=100,y=100)
passwd = Entry(login,width=20,show="*",bd=5)
passwd.place(x=170,y=100)
btn = Button(login, text="Login", command=logindemo).place(x=135,y=150)
cancel = Button(login,text="Cancel", command=cancel).place(x=200,y=150)


login.mainloop();