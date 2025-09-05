class DispositivoEntrada:
    def __init__(self, marca:str, tipo_entrada:str)-> None:
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    # encapsulamiento
    @property
    def marca(self)-> str:
        return self._marca

    @property
    def tipo_entrada(self) -> str:
        return self._tipo_entrada