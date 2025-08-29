# Termometro
# Crea Termometro(celsius=0.0).
# Métodos: a_fahrenheit() y @classmethod desde_fahrenheit(valor) que retorne una instancia en °C.
# Valida que celsius sea numérico.

class Termometro:
    def __init__(self, celsius : float = 0.0) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius
    @celsius.setter
    def celsius(self, valor: float) -> None:
        # validar que sea numerico
        if isinstance(valor,bool) or not isinstance(valor,(int,float)):
            raise ValueError ("Celsius ha de ser numerico")
        self._celsius = float(valor)

    def a_fahrenheit(self) -> float:
        return self._celsius * (9/5) + 32



    @classmethod
    def desde_fahrenheit(cls, valor: float) -> "Termometro":
        if isinstance(valor,bool) or not isinstance(valor,(int,float)):
            raise ValueError ("Fahrenheit ha de ser numerico")
        return cls(celsius=(valor - 32) * (5/9))

    def __repr__(self) -> str:
        return f"Termometro(celsius={self.celsius!r})"

t = Termometro(0.0)
print(t)
print(t.a_fahrenheit())
print(t.desde_fahrenheit(39.2))  # creo el objeto directamente desde la clase

# preguntas
    #porque en la property y setter se ha usar por ejemplo el ._name_atributo y lo mismo en los metodos, porque no usar directamente el self.name_atributo
    # no me queda del todo claro para que es util el classmethod y porque el return se escribe asi? que quiere decir ?
    # en el constructor __init__ el tipo de retorno siempre sera none ?