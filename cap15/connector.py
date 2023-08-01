import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('DROP TABLE Canciones')
cur.execute('CREATE TABLE Canciones (titulo TEXT NOT NULL, reproducciones INTEGER)')
conn.close()