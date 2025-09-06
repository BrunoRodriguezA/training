class Color:
    def __init__(self, color:str) -> None:
        self._color:str = ''
        self.color = color

    @property
    def color(self) -> str:
        return self._color
    @color.setter
    def color(self, valor:str) -> None:
        if not isinstance(valor, str):
            raise TypeError("valor ha de ser una cadena")
        if not valor:
            raise ValueError("No ha de ser un campo vacio")
        self._color = str(valor)

    def __str__(self) -> str:
        return f"Color(color={self.color})"

if __name__ == "__main__":
    c1 = Color('azul')
    print(c1.__dict__)
    print(str(c1))