import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Canciones')
cur.execute('CREATE TABLE Canciones (titulo TEXT NOT NULL UNIQUE, reproducciones INTEGER DEFAULT 0)')
conn.close()