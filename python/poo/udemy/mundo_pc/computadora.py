from python.poo.udemy.mundo_pc.monitor import Monitor
from python.poo.udemy.mundo_pc.teclado import Teclado
from python.poo.udemy.mundo_pc.raton import Raton


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        type(self).contador_computadoras += 1
        self.id_computadora = type(self).contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f""" {self.nombre} : {self.id_computadora}
        Monitor: {self.monitor} 
        Teclado: {self.teclado}
        Raton: {self.raton} """
        # desde el metodo print se va a llamar de manera automatica el str de cada clase

if __name__ == "__main__":
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('Acer', 'bluetooth')
    monitor1 = Monitor('LG', 27)
    pc1 = Computadora('HP', monitor1, teclado1, raton1)
    print(pc1)

    teclado2 = Teclado('HP', 'USB')
    raton2 = Raton('Acer', 'bluetooth')
    monitor2 = Monitor('AOC', 30)
    pc2 = Computadora('Gamer', monitor2, teclado2, raton2)
    print(f'\n{pc2}')