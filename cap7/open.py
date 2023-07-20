archivo = open("mbox-short.txt")
# print(archivo)

count = 0
for linea in archivo:
    if linea.startswith("From "):
        pos_inicial = linea.index(" ") + 1
        pos_final = linea.index(" ", pos_inicial)
        print(linea[pos_inicial:pos_final])
