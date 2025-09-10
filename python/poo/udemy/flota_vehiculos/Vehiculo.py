from abc import ABC, abstractmethod
from typing import List, Dict
from numbers import Real

class Vehiculo(ABC):
    def __init__(self, marca:str, modelo:str) -> None:
        self.marca = marca
        self.modelo = modelo

    @property
    def marca(self) -> str:
        return self._marca
    @marca.setter
    def marca(self, valor:str) -> None:
        if not isinstance(valor, str):
            raise TypeError('marca ha de ser una cadena')
        valor = valor.strip()
        if not valor:
            raise ValueError("marca no ha de ser un campo vacio")
        self._marca = valor

    @property
    def modelo(self) -> str:
        return self._modelo

    @modelo.setter
    def modelo(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise TypeError('modelo ha de ser una cadena')
        valor = valor.strip()
        if not valor:
            raise ValueError("modelo no ha de ser un campo vacio")
        self._modelo = valor

    @abstractmethod
    def coste_viaje(self,dist_kms:float, precios: Dict[str, float]) -> float:
        pass

    @classmethod
    def desde_dict(cls, datos:dict) -> "Vehiculo":
        from .Gasolina import Gasolina
        from .Diesel import Diesel
        from .Electrico import Electrico

        marca = datos.get("marca", "")
        modelo = datos.get("modelo", "")
        consumo_l_100km = datos.get("consumo_l_100km", 0.0)
        tipo_vehiculo = (datos.get("tipo", "")).lower().strip()

        if tipo_vehiculo == "gasolina":
            # pass
            return Gasolina(marca, modelo, consumo_l_100km)
        elif tipo_vehiculo == "diesel":
            # pass
            return Diesel(marca, modelo, consumo_l_100km)
        elif tipo_vehiculo == "electrico":
            # pass
            return Electrico(marca, modelo, consumo_l_100km)
        # si no entra en ningun if retorna None
        else:
            raise ValueError(f"tipo desconocido: {tipo_vehiculo!r}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(marca={self._marca}, modelo={self._modelo})"
