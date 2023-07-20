'''
Utiliza find y una parte de la cadena para extraer la porción de la cadena
después del carácter dos puntos y después utiliza la función float para
convertir la cadena extraída en un número de punto flotante.
'''

str = 'X-DSPAM-Confidence:0.8475'
pos_inicial = str.find(":")

valor = 0
if not pos_inicial == -1:
    valor = float(str[pos_inicial + 1:])
print(valor)