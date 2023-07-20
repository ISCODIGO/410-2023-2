# obtener el dominio del correo de la siguiente linea

linea = 'From stephen.marquard@unah.hn Sat Jan 5 09:14:16 2008'

try:
    pos_inicial = linea.index('@') + 1
    pos_final = linea.find(" ", pos_inicial)
    print(linea[pos_inicial:pos_final])
except ValueError:
    print("No se encontro un dominio valido")
