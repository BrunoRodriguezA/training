import os 
from pathlib import Path
import time 

class CatalogoPeliculas: 
    # ruta_archivo = "C:\\Users\\bruno\\PycharmProjects\\training\\python\\poo\\udemy\\catalogo_peliculas\\servicio\\peliculas.txt"
    ruta_archivo = Path(__file__).parent / "peliculas.txt"
    
    def agregar_peliculas(self, Pelicula) -> None:
        try: 
            with open(self.ruta_archivo, 'a') as f: 
                f.write(f"{Pelicula}\n")
        except Exception as e:
            print(f"{e}, {type(e)}")
    
    def listar_peliculas(self)-> None:
        try: 
            with open(self.ruta_archivo, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print("No existen peliculas en el catalogo")
        except Exception as e:
            print(f"{e}, {type(e)}")
    
    def eliminar(self) -> None:
        try:
            os.remove(self.ruta_archivo)
        except FileNotFoundError:
            print("No existen peliculas en el catalogo")
        except Exception as e: 
            print(f"{e}, {type(e)}")

if __name__ == "__main__":
    catalogo  = CatalogoPeliculas()
    catalogo.agregar_peliculas('Pinocho')
    catalogo.agregar_peliculas('Pepe El Grillo')
    catalogo.agregar_peliculas('Gost')
    catalogo.listar_peliculas()
    time.sleep(5)
    catalogo.eliminar()
    