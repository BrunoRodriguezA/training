class FiguraGeometica:
    def __init__(self, ancho:float, alto:float) -> None:

        self.ancho = ancho
        self.alto = alto

    #ancho
    @property
    def ancho(self) -> float:
        return self._ancho
    @ancho.setter
    def ancho(self, valor:float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("El ancho ha de ser numerico")
        if valor <= 0:
            raise ValueError("Ha de ser un valor mayor que 0")
        self._ancho = float(valor)

    #alto
    @property
    def alto(self) -> float:
        return self._alto
    @alto.setter
    def alto(self, valor:float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise TypeError("El alto ha de ser numerico")
        if valor <= 0:
            raise ValueError("Ha de ser un valor mayor que 0")
        self._alto = float(valor)

    def __str__(self):
        return f"FiguraGeometrica(ancho={self._ancho}, alto={self._alto})"
