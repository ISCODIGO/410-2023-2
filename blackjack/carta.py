from enum import Enum

class Figura(Enum):
    PICAS = 1
    CORAZONES = 2
    TREBOL = 3
    DIAMANTES = 4

class Carta:
    def __init__(self, figura, valor):
        self.figura = figura
        self.valor = valor

    def valor_numerico(self):
        if self.valor == "A":
            return 11
        elif self.valor == "J":
            return 10
        elif self.valor == "Q":
            return 10
        elif self.valor == "K":
            return 10
        else:
            return int(self.valor)

    def __str__(self):
        return f"{self.valor} de {self.figura.name.lower()}"
    
