cadena = "hola mundo"

# uso del operador in
print("in:", "hola" in cadena)

# cuantas veces aparece una subcadena dentro de otra
print("Count:", cadena.count("o"))

# algunas funciones de busqueda
print("startswith:", cadena.startswith("hola"))
print("endswith:", cadena.endswith("mundo"))
print("find:", cadena.find("o", 5))
