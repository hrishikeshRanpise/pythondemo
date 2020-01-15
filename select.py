import sqlite3
conn=sqlite3.connect("new.db")
with conn:
	cur=conn.cursor()
	cur.execute("SELECT * FROM doctor")
	for row in cur.fetchall():
			print("ID"+str(row[0]))
			print("Name"+row[1])
			print("Qual"+row[2])
			#print("Spec"+row[3])