import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM Canciones")
fetch_one = cursor.fetchone()

cursor.execute("SELECT * FROM Canciones")
fetch_many = cursor.fetchmany(2)

cursor.execute("SELECT * FROM Canciones")
fetch_all = cursor.fetchall()

print("Fetch one:", fetch_one)
print("Fetch many:", fetch_many)
print("Fetch all:", fetch_all)

cursor.close()
