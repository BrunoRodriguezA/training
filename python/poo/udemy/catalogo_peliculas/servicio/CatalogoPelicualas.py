import os 
from pathlib import Path
import time 

class CatalogoPeliculas: 
    # ruta_archivo = "C:\\Users\\bruno\\PycharmProjects\\training\\python\\poo\\udemy\\catalogo_peliculas\\servicio\\peliculas.txt"
    ruta_archivo = Path(__file__).parent / "peliculas.txt"

    @classmethod
    def agregar_peliculas(cls, pelicula) -> None:
        try: 
            with open(cls.ruta_archivo, 'a', encoding='utf8') as f:
                f.write(f"{pelicula.nombre}\n")
        except Exception as e:
            print(f"{e}, {type(e)}")

    @classmethod
    def listar_peliculas(cls)-> None:
        try: 
            with open(cls.ruta_archivo, 'r', encoding='utf8') as f:
                print("Catalogo de Peliculas".center(50, '-'))
                print(f.read())
        except FileNotFoundError:
            print("No existen peliculas en el catalogo")
        except Exception as e:
            print(f"{e}, {type(e)}")

    @classmethod
    def eliminar(cls) -> None:
        try:
            os.remove(cls.ruta_archivo)
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
    