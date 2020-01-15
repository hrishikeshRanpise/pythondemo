#vsb = ttk.Scrollbar(root, orient="vertical", command=chat1.yview)
#vsb.place(x=1000, y=170, height=400 + 20)
#chat1.configure(yscrollcommand=vsb.set)
#chat1.place(x=400, y=170)
chat1.pack()
#ttk.Style().configure("Treeview", background="#383838", foreground="coral1")
#ttk.Style().configure("Treeview.heading", background="blue", foreground="palevioletRed1")
#root.configure(background="white")
conn = sqlite3.connect("new.db")
with conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM doctor ORDER BY id DESC')
    for row in cur.fetchall():
        chat1.insert('', 0, text=row[0], values=(row[1], row[2]))
