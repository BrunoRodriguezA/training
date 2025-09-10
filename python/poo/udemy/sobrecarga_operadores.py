class Persona:
    def __init__(self, nombre:str, edad:int) ->None:
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f"{self.nombre} {other.nombre}"

    def __sub__(self, other):
        return self.edad - other.edad


p1 = Persona('Pep', 28)
p2 = Persona('Carlos', 50)
print(p1 + p2)
print(p1 - p2)
#obj1.__add__(obj2)
