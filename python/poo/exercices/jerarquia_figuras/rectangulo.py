from figura import Figura

class Rectangulo(Figura):
    def __init__(self, ancho:float, alto:float):
        super().__init__()
        
        self.ancho = ancho
        self.alto = alto
        
    
    def area(self):
        return round(self.ancho * self.alto,2)
        
    def perimetro(self):
        return round(self.ancho*2 + self.alto*2, 2)

if __name__ == "__main__":
    r1 = Rectangulo(18, 12)
    print(r1.area())
    print(r1.perimetro())