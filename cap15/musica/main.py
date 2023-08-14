import sqlite3
from database import Database

BASE_DATOS = "musica.db"
TABLA = "canciones"


def crear_cancion(manejador: Database):
    titulo = input("Escriba el titulo de la cancion: ")
    autor = input("Escriba el autor de la cancion: ")
    manejador.create(
        {
            "titulo": titulo,
            "autor": autor,
        }
    )


def actualizar_reproducciones(manejador: Database):
    id = int(input("Indique el ID de la cancion a EDITAR: "))
    cancion = manejador.read_one(id)
    reproduciones = int(cancion[3])
    manejador.update(id, {"reproducciones": reproduciones + 1})


def eliminar_cancion(manejador: Database):
    id = int(input("Indique el ID de la cancion a ELIMINAR: "))
    manejador.delete(id)


def imprimir_caciones(manejador: Database):
    datos = manejador.read_many()
    encabezado = tuple(
        manejador.get_column_names()
    )  # tupla para que sea del mismo tipo del contenido
    print(encabezado)
    for fila in datos:
        print(fila)


def main():
    continuar = True
    while continuar:
        print("\n\nCanciones...")
        print("1. Restablecer la Base de Datos")
        print("2. Crear cancion")
        print("3. Aumentar reproducciones")
        print("4. Eliminar cancion")
        print("5. Mostrar todos las canciones")
        print("Para salir presiona cualquier otra opcion")
        opcion = input("Seleccione la opcion: ")

        db = Database(BASE_DATOS, TABLA)

        match opcion:
            case "1":
                db.create_table(
                    [
                        "id INTEGER PRIMARY KEY AUTOINCREMENT",
                        "titulo TEXT NOT NULL",
                        "autor TEXT NOT NULL",
                        "reproducciones INTEGER DEFAULT 0",
                    ]
                )
            case "2":
                print("2")
                crear_cancion(db)
            case "3":
                actualizar_reproducciones(db)
            case "4":
                eliminar_cancion(db)
            case "5":
                imprimir_caciones(db)
            case _:
                exit(0)


# Ejecutar la funcion principal
main()
