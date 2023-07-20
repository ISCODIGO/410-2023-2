def saludar(msg):
    match msg: 
        case "noche":
            print("Es hora de salir")
        case "dias":
            print("Es hora de entrar")
        case _:
            print("Mensaje no identificado")

saludar("hgjhgj")