from enum import Enum
from carta import Carta

class Jugador:
    def __init_(self, nombre: str):
        self.nombre = nombre
        self.mano = []
        self.seguira = True
        self._puntos = 0

    def pedir_carta(self, carta: Carta):
        if self.seguira is True:
            self.mano.append(carta)

    def detenerse(self):
        self.seguira = False

    @property
    def puntos(self):
        self._puntos = 0
        for carta in self.cartas:
            self._puntos += carta.valor_numerico()
        
        return self._puntos
