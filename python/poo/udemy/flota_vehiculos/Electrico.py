from python.poo.udemy.flota_vehiculos.Vehiculo import Vehiculo
from typing import Dict, List
from numbers import Real


class Electrico(Vehiculo):
    def __init__(self, marca, modelo, consumo_l_100km: float) -> None:
        super().__init__(marca, modelo)
        self.consumo_kwh_100km = consumo_l_100km

    @property
    def consumo_kwh_100km(self) -> float:
        return self._consumo_kwh_100km

    @consumo_kwh_100km.setter
    def consumo_kwh_100km(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise TypeError("consumo_kwh_100km ha de ser numerico")
        if valor <= 0:
            raise ValueError("consumo_kwh_100km ha de ser >0")

        self._consumo_kwh_100km = float(valor)

    def coste_viaje(self, dist_kms: float, precios: dict) -> float:
        litros_totales = (dist_kms/100.0)  * self._consumo_kwh_100km
        return litros_totales * float(precios['kwh'])