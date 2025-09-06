# Vector2D
# Crea Vector2D(x, y) con operaciones:
# v1 + v2, v1 - v2, v * escalar (solo escalar numérico), abs(v) (módulo).
# Dunder: __add__, __sub__, __mul__, __abs__, __repr__.
# Valida tipos en operaciones.
import math

class Vector2D:
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        return self._x
    @x.setter
    def x(self, valor:float) -> None:
        if isinstance(valor,bool) or not isinstance(valor,(int,float)):
            raise TypeError("X ha de ser numerico")
        self._x = float(valor)

    @property
    def y(self) -> float:
        return self._y
    @y.setter
    def y(self, valor:float) -> None:
        if isinstance(valor,bool) or not isinstance(valor,(int,float)):
            raise TypeError("Y ha de ser numerico")
        self._y = float(valor)


    # dunder
    def __add__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D): # validacion de tipos
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, escalar: float) -> "Vector2D":
        if isinstance(escalar, bool):
            raise TypeError("Solo se puede multiplicar por un número")
        if not isinstance(escalar, (int, float)): # prueba la version reflejada
            return NotImplemented
        return Vector2D(self.x * escalar, self.y * escalar)

    def __abs__(self) -> float:
        return math.sqrt(self.x**2 + self.y **2)

    def __repr__(self) -> str:
        return f"Vector2D(x={self.x}, y={self.y})"


v1 = Vector2D(2, 1)
# v2 = Vector2D(1, 5)


# print( v1 + v2)
