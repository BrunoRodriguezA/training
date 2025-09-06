from python.poo.udemy.lab_figura_geometrica.Color import Color
from python.poo.udemy.lab_figura_geometrica.FiguraGeometrica import FiguraGeometica


class Rectangulo(FiguraGeometica,Color):
    def __init__(self, ancho:float, alto:float, color:str) -> None:
        FiguraGeometica.__init__(self,ancho, alto)
        Color.__init__(self,color)

    def area(self) -> float:
        return self.ancho * self.alto

    def __str__(self) -> str:
        return f"{FiguraGeometica.__str__(self)} {Color.__str__(self)}"

if __name__ == "__main__":
    r1 = Rectangulo(3,8,'azul')
    print(r1.area())
    print(r1)