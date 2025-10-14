class Pelicula:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre 
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(nombre={self.nombre})" 
    

if __name__ == "__main__":

    p = Pelicula('ScaryMovie')  
    print(p.nombre)
    print(str(p))
    print()