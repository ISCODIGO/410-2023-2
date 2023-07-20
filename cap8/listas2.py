caracteres = list("hola mundo")
print(caracteres)
print("Primer caracter: ", caracteres[0])
print("Ultimo caracter: ", caracteres[-1])

print("For simple...")
for item in caracteres:
    print(item)

print("Enumerate...")
for i, item in enumerate(caracteres):
    if i % 2 == 0:
        print(item)

print("Range (no recomendada)...")
for i in range(len(caracteres)):
    print(caracteres[i])
