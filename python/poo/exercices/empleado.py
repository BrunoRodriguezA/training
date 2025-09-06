from typing import List

class Empleado:

    def __init__(self, nombre:str) -> None:
        self._nombre:str = ""
        self.nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, nombre:str) -> None:
        if not isinstance(nombre, str):
            raise TypeError("Nombre ha de ser una cadena")
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("No puede ser un campo vacio")
        self._nombre = nombre

    def salario(self) -> float:
        raise NotImplementedError("Las subclases deben implementar salario()")

    def __repr__(self) -> str:
        return  f"Empleado(nombre={self.nombre!r})"

class Asalariado(Empleado):
    def __init__(self, nombre:str, salario_mensual:float) -> None:
        # hereda de empleado
        super().__init__(nombre)
        self._salario_mensual = None
        self.salario_mensual = salario_mensual

    @property
    def salario_mensual(self) -> float:
        return self._salario_mensual
    @salario_mensual.setter
    def salario_mensual(self, salario_mensual:float) -> None:
        if isinstance(salario_mensual, bool) or not isinstance(salario_mensual,(int,float)):
            raise TypeError("salario_mensual ha de ser numerico")
        if salario_mensual <= 0:
            raise ValueError("salario_mensual ha de ser mayor que 0")
        self._salario_mensual = float(salario_mensual)

    def salario(self) -> float:
        return self.salario_mensual

    def __repr__(self) -> str:
        return f"Asalariado(nombre={self.nombre!r}, salario={self._salario_mensual})"


class PorHoras(Empleado):
    def __init__(self, nombre:str, tarifa:float, horas:float) -> None:
        super().__init__(nombre)
        self._tarifa = float = 0.0
        self._horas = folat = 0.0

        self.tarifa = tarifa
        self.horas = horas

    @property
    def tarifa(self) -> float:
        return self._tarifa
    @tarifa.setter
    def tarifa(self, tarifa: float) -> None:
        if isinstance(tarifa, bool) or not isinstance(tarifa,(int,float)):
            raise TypeError("Tarifa ha de ser numerico")
        if tarifa <= 0:
            raise ValueError("Tarifa ha de ser mayor que 0")
        self._tarifa = float(tarifa)

    @property
    def horas(self) -> float:
        return self._horas
    @horas.setter
    def horas(self, horas: float) -> None:
        if isinstance(horas, bool) or not isinstance(horas,(int,float)):
            raise TypeError("horas ha de ser numerico")
        if horas <= 0:
            raise ValueError("horas ha de ser mayor que 0")
        self._horas = float(horas)

    def salario(self) -> float:
        return self._tarifa * self._horas

    def __repr__(self) -> str:
        return f"PorHoras(nombre={self.nombre!r}, tarifa={self._tarifa}, horas={self._horas})"

class Empresa:
    def __init__(self, nombre:str) -> None:
        self._nombre = ""
        self._empleados: List[Empleado] = []

        self.nombre = nombre

    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, nombre:str) -> None:
        if not isinstance(nombre, str):
            raise TypeError("Nombre de la Empresa de ser una cadena")
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("No puede ser un campo vacio")
        self._nombre = nombre

    def agregar_empleados(self, empleado: Empleado):
        # validar objeto
        if not isinstance(empleado, Empleado):
            raise TypeError("Solo se pueden agregar instancias Empleado")
        # evitar duplicados
        if any(emp is empleado for emp in self._empleados):
            raise ValueError("Este empleado ya esta en la empresa")
        self._empleados.append(empleado)

    def eliminar_empleado(self, empleado:Empleado):
        if empleado not in self._empleados:
            raise ValueError("Este empleado no esta en la empresa")
        self._empleados.remove(empleado)

    def coste_mensual(self) -> float:
        return sum(e.salario() for e in self._empleados)

    def __repr__(self) -> str:
        return f"Empresa=(nombre={self._nombre}, empleados={len(self._empleados)}"


if __name__ == "__main__":

    e1 = Asalariado('Gio',1000)
    print(repr(e1))
    e2 = PorHoras('Ana', 45, 1)
    e3 = PorHoras('Ana', 45, 1)
    print(repr(e2))

    print(e2 == e3)

    empresa = Empresa('Santander')
    empresa.agregar_empleados(e1)
    empresa.agregar_empleados(e2)
    empresa.agregar_empleados(e3)

    print(repr(empresa))
    print(empresa.coste_mensual())

    empresa.eliminar_empleado(e3)
    print(repr(empresa))
    print(empresa.coste_mensual())



