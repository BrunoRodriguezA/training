class Animal:
    def comer(self):
        print('Como muchas veces al dia')

    def dormir(self):
        print('Duermo muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo Ladrar')

    # sobreesscritura del meth dormir #mismo nombre y parametros
    def dormir(self):
        print('Duermo 15h al día')


animal1 = Animal()
animal1.comer()
animal1.dormir()
print()
perro1 = Perro()
perro1.comer()
perro1.dormir() #metodo sobrescrito de la clase hija
perro1.hacer_sonido()