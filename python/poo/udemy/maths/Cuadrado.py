from python.poo.udemy.Color import Color
from python.poo.udemy.FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #super().__init__(lado) #esta sintxis no es recomenable em herencia multiple, genera confuncion de que clase invocara primero
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self,color)

    def calcular_area(self):
        return self.alto * self.ancho