class Empleado:
    conteo = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.conteo += 1

    def f1():
        print("Metodo de clase")

    @classmethod
    def f2(cls, valor):
        cls.conteo = valor

    @staticmethod
    def f3(x):
        Empleado.conteo = x

if __name__ == '__main__':
    print("Dentro del modulo empleado")
    print(Empleado("Noel", 0))