from python.poo.udemy.sistema_bibliotecas.biblioteca import Biblioteca
from python.poo.udemy.sistema_bibliotecas.libro import Libro

BibliotecaNacional = Biblioteca('Bibilioteca Nacional')
print(BibliotecaNacional.nombre)

# definir los libros
libro1 = Libro('Cien Años de soledad', 'Gabriel Garcia M', 'Ficción')
libro2 = Libro('El amor en los tiempos de colera', 'Gabriel Garcia M', 'Ficción')
libro3 = Libro('Pedro Páramo', 'Juan Rulfo', 'Ficción')
libro4 = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Comedia')
libro5 = Libro('Pantaleón y las visitadoras', 'Mario Vargas Llosa', 'Comedia')

# crear los libros
BibliotecaNacional.agregar_libro(libro1)
BibliotecaNacional.agregar_libro(libro2)
BibliotecaNacional.agregar_libro(libro3)
BibliotecaNacional.agregar_libro(libro4)
BibliotecaNacional.agregar_libro(libro5)

# mostrar info
BibliotecaNacional.buscar_libros_por_autor('Gabriel Garcia M')
print()
BibliotecaNacional.buscar_libros_por_genero('Ficción')
print()
BibliotecaNacional.mostrar_todos_los_libros()
print()

