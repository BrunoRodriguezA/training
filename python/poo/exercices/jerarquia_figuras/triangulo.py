from figura import Figura
from math import sqrt

def desigualdad_triangular(a:float, b:float, c:float) -> bool:
    # lados positivos 
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # identificamos lados mas pequeños y el mas largo
    lados = [a,b,c]
    lado_max = max(lados)
    lados.remove(lado_max)
    return True if sum(lados) >= lado_max else False


class Triangulo(Figura):
    
    def __init__(self, lado_a:float, lado_b:float, lado_c:float) -> None:
        super().__init__()
        
        if not desigualdad_triangular(lado_a,lado_b,lado_c):
            raise ValueError("Lados no forman un triangulo valido")
        
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
    
        
    def area(self):
        a,b,c = self.lado_a, self.lado_b, self.lado_c

        # semiperimetro
        s = (a+b+c)/2.0
        # formula de herón 
        expr = s* (s-a) * (s-b) * (s-c)
        return sqrt(max(expr, 0.0), 2)
        

        
    def perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c