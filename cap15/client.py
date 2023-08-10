import sqlite3
from clase import ManejadorBaseDatos

BASE_DATOS = "musica.db"
TABLA = "canciones"

def crear_cancion(manejador: ManejadorBaseDatos):
    titulo = input("Escriba el titulo de la cancion:")
    autor = input("Escriba el autor de la cancion:")

    data = {
        "titulo": titulo,
        "autor": autor,
    }

    manejador.create(data)

def actualizar_reproducciones(manejador: ManejadorBaseDatos):
    id = int(input("Indique el ID de la cancion a EDITAR: "))
    cancion = manejador.read_one(id)
    reproduciones = int(cancion[2])
    manejador.update({
        "reproducciones": reproduciones + 1
    })


def eliminar_cancion(manejador: ManejadorBaseDatos):
    id = int(input("Indique el ID de la cancion a ELIMINAR: "))
    manejador.delete(id)

def main():
    print('Canciones...')
    print('1. Restablecer la Base de Datos')
    print('2. Crear cancion')
    print('3. Aumentar reproducciones')
    print('4. Eliminar cancion')
    print('5. Mostrar todos las canciones')
    print('Para salir presiona cualquier otra opcion')
    opcion = input("Seleccione la opcion: ")

    db = ManejadorBaseDatos(BASE_DATOS, TABLA)

    match opcion:
        case "1":
            db.construir_tabla([
                "titulo TEXT NOT NULL",
                "autor TEXT NOT NULL",
                "reproducciones INTEGER DEFAULT 0"
            ])
        case "2":
            print("2")
            crear_cancion(db)
        case "3":
            actualizar_cancion(db)
        case "4":
            eliminar_cancion(db)
        case "5":
            datos = db.read_many()
            print(datos)
        case _:
            exit(0)

main()