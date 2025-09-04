# polimorfismo

class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

# Función polimorfica
def hacer_sonido_animal(animal):
    animal.hacer_sonido()


print(f"Clase Padre Animal: ")
animal1 =  Animal()
# animal1.hacer_sonido()
hacer_sonido_animal(animal1)

print(f"\nClase Padre Hija Perro: ")
perro1 = Perro()
# perro1.hacer_sonido()
hacer_sonido_animal(perro1)

print(f"\nClase Padre Hija Gato: ")
gato1 = Gato()
hacer_sonido_animal(gato1)
# gato1.hacer_sonido()

