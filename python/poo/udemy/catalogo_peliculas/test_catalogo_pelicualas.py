from dominio.Pelicula import Pelicula
from servicio.CatalogoPelicualas import CatalogoPeliculas

catalogo = CatalogoPeliculas()

while True:
    print("""Opciones:
        1. Agregar Pelicula
        2. Listar Peliculas
        3. Eliminar catologo de Peliculas 
        4. Salir
        """)
    opcion = int(input("Escribre tu opcion: "))
    
    # if not 1 <= opcion <= 4:     
    if opcion == 4:
        break
    elif opcion == 1: 
        pelicula = Pelicula(input('Proporcione una pelicula: '))
        catalogo.agregar_peliculas(pelicula.nombre)
    elif opcion == 2:
        catalogo.listar_peliculas()
    elif opcion == 3:
        catalogo.eliminar()
        # print('Catalgo de Peliculas eliminado')
    else:
        print('Escoja una opcion correcta')
    
        
        
    
    