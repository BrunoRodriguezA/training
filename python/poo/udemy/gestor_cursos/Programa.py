from typing import List

from python.poo.udemy.gestor_cursos.Curso import Curso
from python.poo.udemy.gestor_cursos.CursoEnVivo import CursoEnVivo
from python.poo.udemy.gestor_cursos.CursoGrabado import CursoGrabado


class Programa:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self._cursos: List[Curso] = []

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

    def agregar_curso(self, curso:Curso) -> None:
        if not isinstance(curso, Curso):
            raise TypeError('No es un curso')
        if any(c is curso for c in self._cursos):
            raise ValueError("Este curso ya esta agregado")
        self._cursos.append(curso)

    def eliminar_curso(self, curso:Curso):
        if not isinstance(curso, Curso):
            raise TypeError('No es un curso')
        if not curso in self._cursos:
            raise ValueError("Este no existe")
        self._cursos.remove(curso)

    def total_horas(self) -> float:
        return sum(curso.carga_horaria() for curso in self._cursos)

    def __repr__(self) -> str:
        return f"Programa(nombre={self._nombre!r}, n_cursos={len(self._cursos)!r})"

if __name__ == "__main__":
    c1 = CursoGrabado('Programacion', 5)
    c2 = CursoEnVivo('Docker', 4.5, 2)
    c3 = ''
    print(c1)
    print(c2)
    p1 = Programa('Bootcamp')
    p1.agregar_curso(c1)
    p1.agregar_curso(c2)
    p1.agregar_curso(CursoGrabado('Programacion', 1))
    p2 = Programa('Udemy')
    print(p1)
    print(p1.total_horas())
    print(f"\n{p2}")

