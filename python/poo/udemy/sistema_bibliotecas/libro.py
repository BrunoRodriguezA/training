class Libro:

    def __init__(self, titulo:str, autor:str, genero:str) -> None:
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    # Atributos de solo lectura
    # titulo
    @property
    def titulo(self) -> str:
        return self._titulo
    # @titulo.setter
    # def titulo(self, titulo:str) -> None:
    #     self._titulo = titulo

    #autor
    @property
    def autor(self) -> str:
        return self._autor
    # @autor.setter
    # def autor(self, autor:str) -> None:
    #     self._autor = autor

    #genero
    @property
    def genero(self) -> str:
        return self._genero
    # @genero.setter
    # def genero(self, genero:str) -> None:
    #     self._genero = genero