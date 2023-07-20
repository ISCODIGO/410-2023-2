lista1 = [10, 20, 30, 40]  # no hay problema de que elementos estan definidos dentro de la lista.
lista2 = list("hola")  # argumento debe ser iterable y solo puede ser uno.

lista1.append(6)
print(lista1)

lista1.insert(1, 4)
print(lista1)

print(len(lista1))

lista1.pop()  # elimina 6
lista1.pop(1)  # elimina 4

print("Lista despues de 2 removes: ", lista1)

lista2.append(True)
lista2.append(2.3)
lista2.append(lista1)
print(lista2)