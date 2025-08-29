# Crea Circulo(radio) con validación radio > 0.
#
# Métodos: area(), circunferencia().
#
# Añade @classmethod desde_diametro(d) que cree el círculo.
import math

class Circulo:

    def __init__(self, radio: float) -> None:
    # dispara los setters
        self.radio = radio

    # radio
    @property
    def radio(self) -> float:
        return self._radio

    @radio.setter
    def radio(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor,(int,float)):
            raise ValueError("El radio ha de ser numero")
        if valor <= 0:
            raise ValueError("El radio ha de ser > 0")
        self._radio = float(valor)

    def area(self) -> float:
        # πr²
        return math.pi * (self._radio ** 2)

    def circunferencia(self) -> float:
        # Circunferencia = 2 * π * 5 cm = 10π cm (aproximadamente 31.42 cm)
        return 2 * math.pi * self._radio

    def __repr__(self) -> str:
        return f"Circulo(radio={self._radio!r})"

    # constructor alternativo en base a la clase principal
    @classmethod
    def desde_diametro(cls, diametro: float) -> "Circulo":
        if diametro <= 0:
            raise ValueError("El diametro debe ser > 0")
        return cls(radio=diametro/2)

# c = Circulo(radio=5)
# print(repr(c))
# print(c.area())
# print(c.circunferencia())

c2 = Circulo.desde_diametro(10)
print(repr(c2))
print(c2.area())


