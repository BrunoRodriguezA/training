# Punto2D
# Crea Punto2D(x, y) con x e y numéricos.
#
# Método: distancia_a(otro_punto) (Euclídea).
#
# Dunder: __repr__ y __eq__ (x e y iguales).
import math

class Punto2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        return self._x
    @x.setter
    def x(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor,(int,float)):
            raise ValueError("X ha de ser numerico")
        self._x = float(valor)

    @property
    def y(self)-> float:
        return  self._y
    @y.setter
    def y(self, valor:float) -> None:
        if isinstance(valor, bool) or not isinstance(valor,(int,float)):
            raise ValueError("Y ha de ser numerico")
        self._y = float(valor)

    # def distancia_a(self, otro_punto: tuple) -> float:
    #     return math.dist((self.x, self.y), otro_punto)
    def distancia_a(self, otro_punto: "Punto2D") -> float: # forward reference
        return math.dist((self.x, self.y), (otro_punto.x, otro_punto.y))

    def __repr__(self) -> str:
        return f"Punto2D(x={self.x}, y={self.y})"

    def __eq__(self, other:object) -> bool:
        if not isinstance(other, Punto2D):
            return False
        return self.x == other.x and self.y == other.y

p1 = Punto2D(1,2)
p2 = Punto2D(4,6)
print(p1)
print(p1.distancia_a(p2))



