# Importing Tkinter module 
from tkinter import * 
from tkinter.ttk import *
  
# Creating root Tkinter window 
root = Tk() 
root.geometry("175x175") 
  
# Tkinter string variable 
# able to store any string value 
v = StringVar(root, "1") 
  
# Dictionary to create multiple buttons 
values = {"Male" : "male", 
          "Female" : "female"} 
  
# Loop is used to create multiple Radiobuttons 
# rather than creating each button separately 
for (text, value) in values.items(): 
    Radiobutton(root, text = text, variable = v, 
        value = value).pack(side = TOP, ipady = 5) 
  
# Infinite loop can be terminated by 
# keyboard or mouse interrupt 
# or by any predefined function (destroy()) 
def radio():
	print("you have selected "+v.get())

btn = Button(root,text="click me",command=radio).pack()


mainloop() 