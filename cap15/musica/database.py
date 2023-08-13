import sqlite3


class Database:

    def __init__(self, archivo: str, tabla: str):
        self.archivo = archivo
        self.table = tabla

    def create_table(self, campos: list):
        with sqlite3.connect(self.archivo) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {self.table}")
            params = ", ".join(campos)
            sql = f"CREATE TABLE {self.table} ({params})"
            cursor.execute(sql)
            conn.commit()

    def create(self, datos: dict):
        with sqlite3.connect(self.archivo) as conn:
            cursor = conn.cursor()
            fields = ", ".join(list(datos.keys()))
            comodines = ['?'] * len(datos)  # hace una lista de ? segun la cantidad de campos
            params = tuple(datos.values())
            sql = f"INSERT INTO {self.table} ({fields}) VALUES({','.join(comodines)})"
            cursor.execute(sql, params)
            conn.commit()

    def read_one(self, id: int) -> any:
        data = None
        with sqlite3.connect(self.archivo) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.table} WHERE id = ?", (id,))
            data = cursor.fetchone()
        return data

    def read_many(self) -> any:
        data = None
        with sqlite3.connect(self.archivo) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.table}")
            data = cursor.fetchall()
        return data

    def update(self, id: int, data: dict):
        with sqlite3.connect(self.archivo) as conn:
            cursor = conn.cursor()

            values = []
            for key in data.keys():
                values.append(f"{key}=?")

            sql = f"UPDATE {self.table} SET {', '.join(values)} WHERE id = ?"
            params = list(data.values())
            params.append(id)
            params = tuple(params)
            cursor.execute(sql, params)
            conn.commit()

    def delete(self, id: int):
        with sqlite3.connect(self.archivo) as conn:
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM {self.table} WHERE id = ?", (id,))
            conn.commit()
