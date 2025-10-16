from dominio.Pelicula import Pelicula
from servicio.CatalogoPelicualas import CatalogoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print("""Opciones:
            1. Agregar Pelicula
            2. Listar Peliculas
            3. Eliminar catologo de Peliculas 
            4. Salir
            """)

        opcion = int(input("Escribre tu opcion(1-4): "))

        if opcion == 1:
            pelicula = Pelicula(input('Proporcione una pelicula: '))
            cp.agregar_peliculas(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar()
            # print('Catalgo de Peliculas eliminado')

    except Exception as e:
        print(f"Error: {e}, {type(e)}")
        opcion = None
    
        
else:
    print("Salimos del Programa...")