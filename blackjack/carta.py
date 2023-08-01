from enum import Enum


class FIGURA(Enum):
    PICAS = 1
    CORAZONES = 2
    TREBOL = 3
    DIAMANTES = 4


class VALOR(Enum):
    AS = 1
    DOS = 2
    TRES = 3
    CUATRO = 4
    CINCO = 5
    SEIS = 6
    SIETE = 7
    OCHO = 8
    NUEVE = 9
    DIEZ = 10
    JOKER = 11
    QUEEN = 12
    KING = 13

    def real_valor(self):
        pass


class Carta:
    def __init__(self, figura: FIGURA, valor: VALOR):
        self.figura = figura
        self.valor = valor

    def valor_numerico(self):
        if self.valor.value == 1:
            return 11
        elif self.valor.value > 10:
            return 10
        else:
            self.valor.value
    
    def __str__(self):
        return f"{self.valor.name.lower()} de {self.figura.name.lower()}"
