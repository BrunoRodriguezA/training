import os 
from pathlib import Path
from snack import Snack

class ServicioSnack:
    _FILENAME = Path(__file__).parent / 'inventario_snacks.txt'
    
    def __init__(self):
        self._snacks = []
        
        if os.path.isfile(type(self)._FILENAME):
            self._snacks = self.obtener_snacks()
        else:
            self.cargar_snacks_iniciales()
    
    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Papas', 70),
            Snack('Refresco', 50),
            Snack('Sandwich', 120)
        ]
        self._snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

        
    def guardar_snacks_archivo(self, snacks):
        try:
            with open(type(self)._FILENAME, 'a') as f:
                for snack in snacks:
                    f.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f"Error al guardar snacks en archivo: {e}, {type(e)}")

    
    def obtener_snacks(self):
        snacks = []
        
        try:
            with open(type(self)._FILENAME, "r") as f:
                print()
                for linea in f:
                    id_snack, nombre, precio = linea.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
                    
        except Exception as e:
            print(f"Error al obtener los snacks: {e}, {type(e)}")
        
        return snacks

        
    def agregar_snacks(self, snack):
        self._snacks.append(snack)
        self.guardar_snacks_archivo([snack])

        
    def mostrar_snack(self):
        for snack in self._snacks:
            print(snack)
    
    
    def get_snacks(self):
        return self._snacks