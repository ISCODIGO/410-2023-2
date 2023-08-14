import sqlite3
import config

# Conectar a la base de datos nuevamente
conn = sqlite3.connect(config.NOMBRE_DB)
cursor = conn.cursor()

# Insertar datos de autores
cursor.execute("INSERT INTO authors (name) VALUES (?)", ('J.K. Rowling',))
cursor.execute("INSERT INTO authors (name) VALUES (?)", ('George Orwell',))

# Obtener el último "author_id" insertado
author_id = cursor.lastrowid

# Insertar datos de libros
cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ('Harry Potter', author_id))
cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", ('1984', 2))

# Confirmar cambios y cerrar la conexión
conn.commit()
conn.close()