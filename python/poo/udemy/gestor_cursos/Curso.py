from abc import ABC, abstractmethod

class Curso(ABC):
    def __init__(self, titulo:str) -> None:
        self.titulo = titulo

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

    @abstractmethod
    def carga_horaria(self) -> float:
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(titulo={self._titulo!r})"