class DispositivoEntrada:
    def __init__(self, marca:str, tipo_entrada:str):
        self.marca = marca
        self.tipo_entrada = tipo_entrada

    # marca
    @property
    def marca(self) -> str:
        return self._marca
    @marca.setter
    def marca(self, marca:str) -> None:
        if not isinstance(marca, str):
            raise TypeError(f"Marca: Ha de ser una cadena")
        if not marca:
            raise ValueError(f"Marca: No se admiten campos vacios")
        self._marca = marca

    # tipoEntrada
    @property
    def tipo_entrada(self) -> str:
        return self._tipo_entrada
    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada:str) -> None:
        if not isinstance(tipo_entrada, str):
            raise TypeError(f"Tipo Entrada: Ha de ser una cadena")
        if not tipo_entrada:
            raise ValueError(f"Tipo Entrada: No se admiten campos vacios")
        self._tipo_entrada = tipo_entrada

    @classmethod
    def crear_usb(cls, marca:str) -> "DispositivoEntrada":
        return cls(marca,'USB')

    def __repr__(self) -> str:
        return f"DispositivoEntrada=(Marca:{self._marca!r}, Tipo Entrada{self._tipo_entrada!r})"

    def __eq__(self, other:object) -> bool:
        if not isinstance(other,DispositivoEntrada):
            return NotImplemented

        return (self._marca == other._marca) and (self._tipo_entrada == other.tipo_entrada)

class Raton(DispositivoEntrada):
    _contador_de_ratones = 0
    def __init__(self, marca, tipo_entrada):
        self._id = type(self)._contador_de_ratones
        type(self)._contador_de_ratones += 1
        super().__init__(marca, tipo_entrada)

    @property
    def id(self) -> int:
        return self._id

    def __repr__(self) -> str:
        return f"Raton=(id:{self._id!r}, marca:{self.marca!r}, tipo_entrada{self.tipo_entrada!r})"


class Teclado(DispositivoEntrada):
    _contador_de_teclados = 0
    def __init__(self, marca, tipo_entrada):
        self._id = type(self)._contador_de_teclados
        type(self)._contador_de_teclados += 1
        super().__init__(marca, tipo_entrada)

    @property
    def id(self) -> int:
        return self._id

    def __repr__(self) -> str:
        return f"Teclado=(id:{self._id!r}, marca:{self.marca!r}, tipo_entrada{self.tipo_entrada!r})"



if __name__ == "__main__":
    # Pruebas
    raton1 = Raton('HP', 'USB')
    print(raton1)
    teclado1 = Teclado('Dell', 'bluetooth')
    print(repr(teclado1))
    usb_stick = DispositivoEntrada.crear_usb('Kingstons')
    print(usb_stick)
    print(raton1 == teclado1)