from python.poo.udemy.sistema_bibliotecas.libro import Libro


class Biblioteca:
    def __init__(self, nombre:str):
        self ._nombre = nombre
        self._libros = []


    def agregar_libro(self, libro: Libro):
        self._libros.append(libro)

    def buscar_libros_por_autor(self, autor:str):
        print(f"Libros de {autor}:")
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)

    def buscar_libros_por_genero(self, genero:str):
        print(f"Libros de {genero}:")
        for libro in self._libros:
            if libro.genero.lower() == genero.lower():
                self.mostrar_libro(libro)

    def mostrar_todos_los_libros(self):
        print(f"Todos los libros de la {self._nombre}:")
        for libro in self._libros:
            self.mostrar_libro(libro)

    def mostrar_libro(self, libro:Libro):
        print(f"Libro -> Titulo: {libro.titulo}, Autor: {libro.autor}, Genero: {libro.genero}")

    @property
    def nombre(self) -> str:
        return self._nombre
    # @nombre.setter
    # def nombre(self, nombre) -> None:
    #     self._nombre = nombre

    @property
    def libros(self):
        return self._libros
    # @libros.setter
    # def libros(self, libros) -> None:
    #     self._libros = libros

