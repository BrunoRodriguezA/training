from python.poo.udemy.lab_figura_geometrica.Color import Color
from python.poo.udemy.lab_figura_geometrica.FiguraGeometrica import FiguraGeometica


class Cuadrado(FiguraGeometica, Color):
    def __init__(self, lado:float, color:str) -> None:
        FiguraGeometica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def calcular_area(self) -> float:
        return self.ancho * self.alto

    def __str__(self) -> str:
        return f"{FiguraGeometica.__str__(self)} {Color.__str__(self)}"
if __name__ == "__main__":
    c1 = Cuadrado(5,'verde')
    print(c1)
    print(c1.calcular_area())
