'''
C -create
R - read
U - update
D - delete
'''

import sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# create
cur.execute('INSERT INTO Canciones (titulo, reproducciones) VALUES (?, ?)',
('Thunderstruck', 20))
cur.execute('INSERT INTO Canciones (titulo, reproducciones) VALUES (?, ?)',
('My Way', 15))
conn.commit()

# update
cur.execute("UPDATE Canciones SET reproducciones = ? WHERE titulo = ?", (50, "Prueba"))
conn.commit()

# read
print('Canciones:')
cur.execute('SELECT titulo, reproducciones FROM Canciones')
for fila in cur:
    print(fila)


# delete
print("Delete...")
cur.execute('DELETE FROM Canciones WHERE reproducciones < 100')
conn.commit()

cur.close()