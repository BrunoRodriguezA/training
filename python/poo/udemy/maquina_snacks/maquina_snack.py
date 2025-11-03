from servicio_snack import ServicioSnack
from snack import Snack

class MaquinaSnacks:
    def __init__(self):
        self.servicion_snacks = ServicioSnack()
        self.productos = []
        
    def maquina_snacks(self):
        salir = False
        print("Manquina de snacks")
        self.servicion_snacks.mostrar_snack()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Ocurrio un error: {e}")    
    
    def mostrar_menu(self):
        print(f""" Menu:
              1 - Comprar snack 
              2 - Mostrat ticket 
              3 - Agregar Nuevo Snack al inventario 
              4 - Inventario Snacks 
              5 - Salir
              """)
        return int(input("Elige una opción: "))
    
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion ==2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicion_snacks.mostrar_snack()
        elif opcion == 5:
            print('Regresa Pronto')
            return True
        else:
            print(f"Opcion invalida: {opcion}")
        
        return False
    
    def comprar_snack(self):
        id_snack = int(input("Que snack quieres comprar (id)?: "))
        snacks = self.servicion_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        
        if snack:
            self.productos.append(snack)
            print(f"Snack encontrado: {snack}")
            
        else:
            print(f"Id snack no encontrado: {id_snack}")
            
    def mostrar_ticket(self):
        if not self.productos:
            print("No hay snacks en el ticket")
            return
        
        total = sum(snack.precio for snack in self.productos)
        print('---ticket de venta---')
        for producto in self.productos:
            print(f'\t- {producto.nombre} - ${producto.precio:.2f}')
        print(f'\tTotal -> ${total:.2f}')
        
    def agregar_snack(self):
        nombre = input('Nombre del snack: ')
        precio = float(input('Precio del snack: '))
        nuevo_snack = Snack(nombre, precio)
        self.servicion_snacks.agregar_snacks(nuevo_snack)
        print('Snack agregado correctamente.')
        
        
if __name__ == "__main__":
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()
    # print(maquina_snack)
