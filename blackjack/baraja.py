import random
from carta import Carta, FIGURA, VALOR

class Baraja:
    def __init__(self) -> None:
        self.cartas = []
        self.actual = 0
        # crear las 52 cartas
        for figura in FIGURA:
            for v in VALOR:
                self.cartas.append(
                    Carta(valor=v, figura=figura)
                )
        self.mezclar()
    
    def mezclar(self):
        """
        Organiza aleatoriamente las cartas para que no un orden especifico
        """
        for i, _ in enumerate(self.cartas):
            aleatorio = random.randint(0, 51)
            self.cartas[i], self.cartas[aleatorio] = self.cartas[aleatorio], self.cartas[i]

    def pedir(self) -> Carta:
        """
        Devolver una carta
        """
        _actual = self.actual
        self.actual += 1
        try:
            return self.cartas[_actual]
        except IndexError:
            '''
            1. Lanzar un error y detener el juego.
            2. Barajar de nuevo y seguir jugando.
            '''
            self.mezclar()
            self.actual = 0
            return self.pedir()
    