# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 0  1  2  3  4  5  6  7   8   9

n = int(input("Elegir valor de n: "))
conteo = 1
penultimo = 0
ultimo = 1
actual = 0
while conteo <= n:
    actual = penultimo + ultimo
    penultimo = ultimo
    ultimo = actual
    conteo += 1

print("El fibonacci es", actual)