from tkinter import *
from tkinter import ttk
import sqlite3


root = Tk()
root.title("Doctors")
root.geometry("800x800")

chat1 = ttk.Treeview(root,height=20 , columns=('NAME', 'QUAL', 'SPEC'), selectmode="extended")
chat1.heading('#0', text='ID', anchor=CENTER)
chat1.heading('#1', text='DOCTORNAME', anchor=CENTER)
chat1.heading('#2', text='QUAL', anchor=CENTER)
chat1.heading('#3', text="SPEC", anchor=CENTER)
chat1.column('#1', stretch=YES, minwidth=50, width=100)
chat1.column('#3', stretch=YES, minwidth=50, width=200)
chat1.column('#2', stretch=YES, minwidth=50, width=200)
chat1.column('#0', stretch=YES, minwidth=50, width=100)
chat1.pack()

conn = sqlite3.connect("new.db")
with conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM doctor ORDER BY id DESC')
    for row in cur.fetchall():
        chat1.insert('', 0, text=row[0], values=(row[1], row[2]))

root.mainloop()