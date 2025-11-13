from numbers import Real

class Snack:
    _contador = 0
    
    def __init__(self, nombre:str, precio:float) -> None: 
        type(self)._contador += 1
        
        self._id_snack = type(self)._contador
        self.nombre = nombre
        self.precio = precio

    # id
    @property
    def id_snack(self) -> int:
        return self._id_snack
    
    # nombre        
    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, value:str) -> None:
        self._nombre = value 
        
    # precio 
    @property
    def precio(self) -> float:
        return self._precio
    @precio.setter
    def precio(self, value:float) -> None:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError('precio ha de ser numerico')
        elif value < 0:
            raise ValueError('precio ha de ser > 0')
        
        self._precio = value
    
    
    def __str__(self) -> str:
        return f'Id: {self.id_snack}, Nombre: {self.nombre}, Precio:{self.precio}'

    def __repr__(self):
        return  f'{type(self).__name__}(Id:{self.id_snack!r}, Nombre:{self.nombre!r}, Precio:{self.precio!r})'      
        
if __name__ == "__main__":
    s1 = Snack('papas', 1.0)
    s2 = Snack('refresco', 10)
    
    print(s1)
    print(s2)