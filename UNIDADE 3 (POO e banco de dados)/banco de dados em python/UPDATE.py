import sqlite3

conn = sqlite3.connect('aulaDB.db')
cursor = conn.cursor()

cursor.execute("UPDATE fornecedor SET id_fornecedor = 1 WHERE id_fornecedor = 2")
conn.commit()

cursor.execute("SELECT * FROM fornecedor")
for linha in cursor.fetchall():
    print(linha)

cursor.close()
conn.close()