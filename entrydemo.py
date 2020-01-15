from tkinter  import*

root = Tk()
root.title("Entry Demo")
root.geometry("400x300")

lbl1 = Label(root,text="Name").place(x=40,y=40)

ent1 = Entry(root,)
ent1.place(x= 100,y=40)

def disp():
	print(""+ent1.get())

btn1 = Button(root, text="Display name", command=disp)
btn1.place(x= 70,y=80)


root.mainloop()

#ent1.delete(0,END) to clear the entry field

#ent1.get() to get the text from the entry field