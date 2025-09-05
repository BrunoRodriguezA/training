from python.poo.udemy.mundo_pc.computadora import Computadora
from python.poo.udemy.mundo_pc.monitor import Monitor
from python.poo.udemy.mundo_pc.orden import Orden
from python.poo.udemy.mundo_pc.raton import Raton
from python.poo.udemy.mundo_pc.teclado import Teclado

# titulo
print("***Mundo PC***")

# definimos perifericos
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('Acer', 'bluetooth')
monitor1 = Monitor('LG', 27)
pc1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('HP', 'USB')
raton2 = Raton('Acer', 'bluetooth')
monitor2 = Monitor('AOC', 30)
pc2 = Computadora('Gamer', monitor2, teclado2, raton2)


teclado3 = Teclado('Dell', 'USB')
raton3 = Raton('Dell', 'bluetooth')
monitor3 = Monitor('Dell', 19)
pc3 = Computadora('Dell', monitor3, teclado3, raton3)


computadoras_1 = [pc1,pc2]
# se crea la orden
orden1 = Orden(computadoras_1)
# agregamos otra pc a nuestra orden
orden1.agregar_computadoras(pc3)

print(orden1)
# orden.__str__()

