archivo = open("datos.txt", mode="w")

for _ in range(3):
    archivo.write("POO\n")

archivo.close()