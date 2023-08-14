import sqlite3
import config

# Conectar a la base de datos nuevamente
conn = sqlite3.connect(config.NOMBRE_DB)
cursor = conn.cursor()

# Obtener todos los autores
cursor.execute("SELECT * FROM authors")
autores = cursor.fetchall()
print("Autores:")
for autor in autores:
    print(autor)

# Obtener todos los libros con sus autores
cursor.execute("SELECT books.title, authors.name FROM books INNER JOIN authors ON books.author_id = authors.id")
libros_con_autores = cursor.fetchall()
print("\nLibros con Autores:")
for libro in libros_con_autores:
    print(libro)

# Cerrar la conexión
conn.close()
