from python.poo.udemy.lab_figura_geometrica.Cudrado import Cuadrado
from python.poo.udemy.lab_figura_geometrica.FiguraGeometrica import FiguraGeometica
from python.poo.udemy.lab_figura_geometrica.Rectangulo import Rectangulo

# no se puede instanciar una clase abstracta
# figura = FiguraGeometica()

print("Cuadrado".center(50, '-'))
c1 = Cuadrado(5,'rojo')
print(c1.calcular_area())
print(c1)

print("Rectangulo".center(50,'-'))
r1 = Rectangulo(3,8,'verde')
print(r1.calcular_area())
print(r1)

print(Cuadrado.mro())