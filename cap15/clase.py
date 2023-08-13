import sqlite3


class ManejadorBaseDatos:

    def __init__(self, archivo: str, tabla: str):
        self.connector = sqlite3.connect(archivo)
        self.table = tabla

    def construir_tabla(self, campos: list):
        cursor = self.connector.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {self.table}")
        parametros = ", ".join(campos)
        comando = f"CREATE TABLE {self.table} ({parametros})"
        cursor.execute(comando)
        self.connector.commit()
        cursor.close()

    def create(self, datos: dict):
        cursor = self.connector.cursor()
        campos = ", ".join(list(datos.keys()))
        comodines = ['?'] * len(datos)  # hace una lista de ? segun la cantidad de campos
        valores = tuple(datos.values())
        comando = f"INSERT INTO {self.table} ({campos}) VALUES({','.join(comodines)})"
        cursor.execute(comando, valores)
        self.connector.commit()
        cursor.close()

    def read_one(self, id: int) -> any:
        cursor = self.connector.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE id = ?", (id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    def read_many(self) -> any:
        cursor = self.connector.cursor()
        cursor.execute(f"SELECT * FROM {self.table}")
        data = cursor.fetchall()
        cursor.close()
        return data

    def update(self, id: int, datos: dict):
        cursor = self.connector.cursor()

        valores = []
        for clave in datos.keys():
            valores.append(f"{clave}=?")

        comando = f"UPDATE {self.table} SET {', '.join(valores)} WHERE id = ?"
        argumentos = list(datos.values())
        argumentos.append(id)
        cursor.execute(comando, tuple(argumentos))
        self.connector.commit()
        cursor.close()

    def delete(self, id: int):
        cursor = self.connector.cursor()
        cursor.execute(f"DELETE FROM {self.table} WHERE id = ?", (id,))
        self.connector.commit()
        cursor.close()
