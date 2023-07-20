archivo = open("mbox.txt")
# print(archivo)

bandera = 0
for linea in archivo:
    if linea.startswith("X-DSPAM-Confidence: "):
        pos_inicial = linea.index(" ") + 1
        palabra = linea[pos_inicial:]
        confianza = float(palabra)

        if bandera < confianza:
            bandera = confianza
print(bandera)