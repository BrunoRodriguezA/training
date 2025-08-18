# Rectangulo
# Crea Rectangulo(ancho, alto) con @property y validación > 0.
#
# Métodos: area(), perimetro(), es_cuadrado() (bool).
#
# Añade __repr__ con dimensiones.

class Rectangulo:
    def __init__(self, ancho: float, alto: float):
        # dispara los setters
        self.ancho = ancho
        self.alto = alto

    # --- ancho ---
    @property
    def ancho(self) -> float:
        return self._ancho
    @ancho.setter
    def ancho(self, valor:float) -> None:
        if isinstance(valor,bool) or not isinstance(valor,(int,float)):
            raise ValueError("El ancho ha de ser numerico (int o float)")
        if valor <= 0:
            raise ValueError("El ancho ha de ser > 0")
        self._ancho = float(valor)

    # --- alto ---
    @property
    def alto(self) -> float:
        return self._alto
    @alto.setter
    def alto(self, valor: float) -> None:
        if isinstance(valor,str) or (isinstance(valor,bool) and not isinstance(valor,(int,float))):
            raise ValueError("El alto ha de ser numerico (int o float)")
        if valor <= 0:
            raise ValueError("El alto ha de ser > 0")
        self._alto = float(valor)

    # --- area ---
    def area(self) -> float:
        area = self._ancho * self._alto  #se usa variable local o return directo
        return area

    # --- perimetro ---
    def perimetro(self) -> float:
        return 2 * (self._alto + self._ancho)

    # --- es_cuadrado ---
    def es_cuadrado(self) -> bool:
        return self._alto == self._ancho

    def __repr__(self) -> str:
        return f"Rectangulo(ancho={self._ancho!r}, alto={self._alto!r})"

# test
r = Rectangulo(2,5)
print(r.area())
print(r.perimetro())
print(r.es_cuadrado())
print(repr(r))

#dudas
# que son la variables locales ?
# porque en el metodo area se hace el calculo directamente, mi idea era guardar el resultado en un variable (self.area) y luego retornarla
# lo de solo anotan y no asignan no lo entiendo
