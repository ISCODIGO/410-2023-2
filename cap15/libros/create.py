import sqlite3
import config

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect(config.NOMBRE_DB)
cursor = conn.cursor()

# Crear la tabla "authors"
cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
                  id INTEGER PRIMARY KEY,
                  name TEXT
                )''')

# Crear la tabla "books" con "author_id" como clave foránea que hace referencia a la tabla "authors"
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                  id INTEGER PRIMARY KEY,
                  title TEXT,
                  author_id INTEGER,
                  FOREIGN KEY (author_id) REFERENCES authors(id)
                )''')

# Confirmar cambios y cerrar la conexión
conn.commit()
conn.close()
