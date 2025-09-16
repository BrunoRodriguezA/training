# catalogar elemntos y buscar

from abc import ABC, abstractmethod
from numbers import Integral
from typing import List
from datetime import datetime
from datetime import date

class Item(ABC):
    def __init__(self, titulo: str, anio:int) -> None:
        self.titulo = titulo
        self.anio = anio
        ...

    # titulo
    @property
    def titulo(self) -> str:
        return self._titulo
    @titulo.setter
    def titulo(self, valor:str) -> None:
        if not isinstance(valor, str):
            raise TypeError('titulo ha de ser una cadena')
        valor = valor.strip()
        if not valor:
            raise ValueError('titulo no ha de ser un campo vacio')
        self._titulo = str(valor)

    #anio
    @property
    def anio(self) -> int:
        return self._anio
    @anio.setter
    def anio(self, valor:int) -> None:
        if isinstance(valor,bool) or not isinstance(valor, Integral):
            raise TypeError("anio ha de ser numerico")
        if valor <= 0:
            raise ValueError("anio ha de ser >0")
        current_year = date.today().year
        if not (800 <= valor <= current_year):
            raise ValueError("anio ha de ser razonable")
        self._anio = int(valor)

    @abstractmethod
    def description(self) -> str:
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(titulo={self.titulo!r}, año={self.anio!r})"

class Libro(Item):
    def __init__(self,titulo:str, anio:int, autor:str, paginas: int) -> None:
        super().__init__(titulo, anio)
        self.autor = autor
        self.paginas = paginas

    # autor
    @property
    def autor(self) -> str:
        return self._autor
    @autor.setter
    def autor(self, valor:str) -> None:
        if not isinstance(valor, str):
            raise TypeError('autor ha de ser una cadena')
        valor = valor.strip()
        if not valor:
            raise ValueError('autor no ha de ser un campo vacio')
        self._autor = str(valor)

    # paginas
    @property
    def paginas(self) -> int:
        return self._paginas
    @paginas.setter
    def paginas(self, valor:int) -> None:
        if isinstance(valor,bool) or not isinstance(valor,Integral):
            raise TypeError("paginas ha de ser numerico")
        if valor <= 0:
            raise ValueError("paginas ha de ser >0")
        self._paginas = int(valor)

    def description(self) -> str:
        return f"Libro=(titulo={self._titulo!r}, autor={self._autor!r}, paginas={self._paginas!r}, anio={self._anio!r})"


class Pelicula(Item):
    def __init__(self, titulo:str, anio:int, director:str, duracion_min:int) -> None:
        super().__init__(titulo, anio)
        self.director = director
        self.duracion_min = duracion_min

    # director
    @property
    def director(self) -> str:
        return self._director
    @director.setter
    def director(self, valor:str) -> None:
        if not isinstance(valor, str):
            raise TypeError('director ha de ser una cadena')
        valor = valor.strip()
        if not valor:
            raise ValueError('director no ha de ser un campo vacio')
        self._director = str(valor)

    # duracion_min
    @property
    def duracion_min(self) -> int:
        return self._duracion_min
    @duracion_min.setter
    def duracion_min(self, valor:int) -> None:
        if isinstance(valor,bool) or not isinstance(valor,Integral):
            raise TypeError("duracion_min ha de ser numerico")
        if valor <= 0:
            raise ValueError("duracion_min ha de ser >0")
        self._duracion_min = int(valor)

    def description(self) -> str:
        return f"Pelicula(titulo={self._titulo!r}, director={self._director!r}, duracion_min={self._duracion_min!r}, anio={self._anio!r})"

class Catalago:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self._catalogo: List[Item] = []
    # nombre
    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, valor:str) -> None:
        if not isinstance(valor, str):
            raise TypeError('nombre ha de ser una cadena')
        valor = valor.strip()
        if not valor:
            raise ValueError('nombre no ha de ser un campo vacio')
        self._nombre = str(valor)


    def agregar(self, item: Item) -> None:
        if not isinstance(item, Item):
            raise TypeError("Ha de ser un Item")
        if any(i is item for i in self._catalogo):
            raise ValueError("Item ya existe en el catalogo")
        self._catalogo.append(item)
    def eliminar(self, item: Libro|Pelicula) -> None:
        if not isinstance(item, Item):
            raise TypeError("Ha de ser un item valido")
        if not item in self._catalogo:
            raise ValueError("Item no existe en el catalogo")
        self._catalogo.remove(item)

    def buscar_por_titulo(self, substring:str) -> List[Item]:
        coincidencias = []
        substring = substring.strip().lower()
        for item in self._catalogo:
            if substring in item.titulo.lower():
                coincidencias.append(item)
        return coincidencias

    def __len__(self) -> int:
        return len(self._catalogo)

    def __iter__(self):
        return iter(self._catalogo)

    def __contains__(self, item:Item) -> bool:
        return item in self._catalogo

    def __getitem__(self, idx: int) -> Item:
        return self._catalogo[idx]

    def __repr__(self) -> str:
        return f"Catalogo(nombre={self._nombre!r}, n_catalogo={len(self._catalogo)})"


if __name__ == "__main__":
    # e1 = Item('pinocho', 2000
    libro1 = Libro('Pantaleon y las visitadoras', 2000, 'Vargas Llosa', 200)
    pelicula1 = Pelicula('Transformer', 2004, 'Steven Spilver', 120)
    libro2 = Libro('Pinocho', 1826, 'Carlo Collodi', 20)
    pelicula2 = Pelicula('IT', 2013, 'Steven King', 120)


    cat = Catalago('MiCatalogo')
    cat.agregar(libro1)
    cat.agregar(libro2)
    cat.agregar(pelicula2)
    # print(cat)
    #
    # print(len(cat))
    # for item in cat:
    #     print(item.description())
    #
    # libros_it = cat.buscar_por_titulo("in")
    # if libros_it:
    #     print("Encontrado", len(libros_it))

    primero = cat[0]
    print(primero.titulo)

    print(primero in cat)