from abc import ABC, abstractmethod
from numbers import Real
from typing import Callable, List
from statistics import mean

from numpy.ma.extras import average


class Sensor(ABC):
    def __init__(self, id:str, fuente: Callable[[], float]) -> None:
        self.id = id
        self.fuente = fuente

    # id
    @property
    def id(self) -> str:
        return self._id
    @id.setter
    def id(self, valor:str) -> None:
        if not isinstance(valor,str):
            raise TypeError("id ha de ser una cadena")
        valor = valor.strip()
        self._id = str(valor)

    # fuente
    @property
    def fuente(self) -> Callable[[], float]:
        return self._fuente
    @fuente.setter
    def fuente(self, fn: Callable[[], float]) -> None:
        if not callable(fn):
            raise TypeError("fuente ha de ser callable sin args")
        self._fuente = fn

    #help de lectura cruda con validacion tipo
    def _leer_cruda(self) -> float:
        valor = self._fuente()
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise TypeError("la fuente ha de ser numerico")
        return float(valor)

    @abstractmethod
    def leer(self) -> float:
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self._id!r})"

class SensorTemperatura(Sensor):
    def __init__(self, id:str, fuente:Callable[[], float], offset:float) -> None:
        super().__init__(id, fuente)
        self.offset = offset

    @property
    def offset(self) -> float:
        return self._offset
    @offset.setter
    def offset(self, valor:float) -> None:
        if isinstance(valor,bool) or not isinstance(valor,(int,float)):
            raise TypeError("offset ha de ser numerico")
        self._offset = float(valor)

    def leer(self) -> float:
        return self._leer_cruda() + self._offset

class SensorHumedad(Sensor):
    def __init__(self, id:str, fuente:Callable[[], float], factor:float) -> None:
        super().__init__(id, fuente)
        self.factor = factor

    @property
    def factor(self) -> float:
        return self._factor
    @factor.setter
    def factor(self, valor:float) -> None:
        if isinstance(valor,bool) or not isinstance(valor,(int,float)):
            raise TypeError("factor ha de ser numerico")
        if valor <= 0:
            raise ValueError("factor ha de ser >0")
        self._factor = float(valor)

    def leer(self) -> float:
        return self._leer_cruda() * self._factor

class Estacion():
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
        self._estaciones: List[Sensor] = []

    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, valor:str) -> None:
        if not isinstance(valor,str):
            raise TypeError("nombre ha de ser una cadena")
        valor = valor.strip()
        if not valor:
            raise ValueError("nombre no ha de ser un campo vacio")
        self._nombre = valor

    def agregar_sensores(self, sensor:Sensor) -> None:
        if not isinstance(sensor, Sensor):
            raise TypeError("No es un sensor")
        if any(x is sensor for x in self._estaciones):
            raise ValueError("Sensor ya existe")

        self._estaciones.append(sensor)

    def promedio(self) -> float:
        if not self._estaciones:
            raise ValueError("no hay sensores para promediar")
        return mean((s.leer() for s in self._estaciones))

    def __len__(self) -> int:
        return len(self._estaciones)

    def __iter__(self):
        return iter(self._estaciones)

    def __repr__(self) -> str:
        return f"Estaciones(nombre={self._nombre}, n_sensores={len(self._estaciones)})"

if __name__ == "__main__":
    t1 = SensorHumedad('t1', lambda : 10.0, 0.7)
    t2 = SensorTemperatura('t2', lambda : 10.0, 0.7)
    t3 = SensorTemperatura('t3', lambda : 10.0, 0.7)
    print(t1, t1.leer())
    print(t2, t2.leer())
    print(t3, t3.leer())
    e1 = Estacion('MiEstacion')
    e1.agregar_sensores(t1)
    e1.agregar_sensores(t2)
    e1.agregar_sensores(t3)
    print(e1, "promedio:", e1.promedio())