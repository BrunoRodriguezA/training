from figura import Figura
from math import pi

class Circulo(Figura):
    def __init__(self, r:float):
        super().__init__()
        self.r = r
    
    @property
    def r(self) -> float:
        return self._r
    @r.setter
    def r(self, valor:float) -> None:
        self._r = valor 
    
    def area(self):
        return round(pi * self.r**2, 2)
        
    def perimetro(self):
        return round(2 * pi * self.r, 2)

if __name__ == "__main__":
    c1 = Circulo(.5)
    print(c1.area())
    print(c1.perimetro())