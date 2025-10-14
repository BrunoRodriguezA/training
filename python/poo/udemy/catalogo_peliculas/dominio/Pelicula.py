class Pelicula:
    def __init__(self, nombre:str) -> None:
        self._nombre = nombre
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(nombre={self.nombre})" 

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor:str) -> None:
        self._nombre = valor

if __name__ == "__main__":
    p = Pelicula('ScaryMovie')  
    print(p.nombre)
    print(str(p))
    print()