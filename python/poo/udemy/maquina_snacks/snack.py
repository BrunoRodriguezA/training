from typing import Optional

class Snack:
    _contador_snack = 0
    
    def __init__(self, nombre:Optional[str]=None, precio:float=0.0):
        type(self)._contador_snack +=1 
        self._id_snack = type(self)._contador_snack
        self.nombre = nombre
        self.precio = precio
        
    @property
    def id_snack(self) -> int:
        return self._id_snack
        
    @property
    def nombre(self) -> Optional[str]:
        return self._nombre 
    @nombre.setter
    def nombre(self, value:Optional[str]) -> None:
        self._nombre = value
        
    @property
    def precio(self) -> float:
        return self._precio
    @precio.setter
    def precio(self, value:float) -> None:
        self._precio = value
        
    def escribir_snack(self):
        return f'{self._id_snack},{self.nombre},{self.precio}'

    def __str__(self) -> str:
        return f"{type(self).__name__}: id_snack={self._id_snack}, nombre={self.nombre}, precio={self.precio}"
    
            
if __name__ == "__main__":
    s1 = Snack('nueces', 2.5)
    print(str(s1))
    s2 = Snack('galleta', 2.5)
    print(str(s2))
    
    print(s1.escribir_snack())
    