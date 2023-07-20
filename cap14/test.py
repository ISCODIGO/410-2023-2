import empleado as emp

x = emp.Empleado("Ana", 0)
x.cargo = "Analista"



y = emp.Empleado("Ana", 0)
print(x.__dict__)
print(y.__dict__)

print(emp.Empleado.conteo)
emp.Empleado.f1()
emp.Empleado.f2(10)

print(emp.Empleado.conteo)
emp.Empleado.f3(20)

print(emp.Empleado.conteo)
