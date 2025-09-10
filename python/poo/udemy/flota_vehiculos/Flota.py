from python.poo.udemy.flota_vehiculos.Diesel import Diesel
from python.poo.udemy.flota_vehiculos.Electrico import Electrico
from python.poo.udemy.flota_vehiculos.Gasolina import Gasolina
from python.poo.udemy.flota_vehiculos.Vehiculo import Vehiculo
from typing import List
class Flota:
    def __init__(self, nombre):
        self.nombre = nombre
        self._listado_vehiculos: List[Vehiculo] = []

    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise TypeError('nombre, ha de ser una cadena')
        valor = valor.strip()
        if not valor:
            raise ValueError('nombre no puede ser un campo vacio')
        self._nombre = valor

    def agregar_vehiculo(self, veh: Vehiculo) -> None:
        if not isinstance(veh, Vehiculo):
            raise TypeError("Solo vehiculo")
        if any(v is veh for v in self._listado_vehiculos):
            raise ValueError("Vehiculo ya agregado")
        self._listado_vehiculos.append(veh)

    def eliminar_vehiculo(self, veh: Vehiculo) -> None:

        if veh not in self._listado_vehiculos:
            raise ValueError("el vehiculo no se encuentra en la flota")
        self._listado_vehiculos.remove(veh)

    def coste_total(self, dist_km:float, precios:dict) -> float:
        return sum(veh.coste_viaje(dist_km, precios) for veh in self._listado_vehiculos)

    def __repr__(self) -> str:
        return f"Flota(nombre={self._nombre!r}, n_vehiclos={len(self._listado_vehiculos)})"


if __name__ == "__main__":
    v1 = Gasolina('Citroen','C3',7)
    v2 = Diesel('Peugeot','C1',4)
    v3 = Electrico('Opel','Moka',8)

    print(repr(v3))
    print(repr(v1))
    print(repr(v2))

    # precios = {"gasolina": 1.8, "diesel": 1.7, "kwh": 0.25}
    #
    # europa_car = Flota('EuropaCar')
    # for v in (v1,v2,v3):
    #     europa_car.agregar_vehiculo(v)
    #
    # print(europa_car)
    # print(europa_car.coste_total(200, precios))