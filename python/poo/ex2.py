# Crea CuentaBancaria(titular, saldo=0.0). Debe:
# Validar titular no vacío, saldo >= 0.
# Métodos: depositar(monto>0), retirar(monto>0) sin permitir saldo negativo, mostrar().
# Lanza ValueError si se viola alguna regla. Añade __repr__.
from typing import Optional

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self._titular: str = ""
        self._saldo: float = 0.0

        self.titular = titular
        self.saldo = saldo

    # --- titular ---
    @property
    def titular(self) -> str:
        return self._titular
    @titular.setter
    def titular(self, valor: str) -> None:
        if not isinstance(valor,str):
            raise ValueError("El titular debe de ser una cadena")
        valor = valor.strip()
        if not valor:
            raise ValueError("El titular no puede estar vacio")
        self._titular = valor

    # --- saldo ---
    @property
    def saldo(self) -> float:
        return self._saldo
    @saldo.setter
    def saldo(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, (int,float)):
            raise ValueError("El saldo debe de ser numerico (int o float")
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(valor)

    # -- en las operaciones conviene verificar si es numerico y no bool | amtosoàr str por error
    # depositar
    def depositar(self, monto: float) -> None:
        if isinstance(monto, bool) or not isinstance(monto, (int,float)):
            raise ValueError("El monto debe de ser numerico (int o float")
        if monto <= 0:
            raise ValueError("El deposito debe ser >0")
        self.saldo += float(monto)

    # retirar
    def retirar(self, monto):

        if isinstance(monto, bool) or not isinstance(monto, (int,float)):
            raise ValueError("El monto debe de ser numerico (int o float")
        if monto <= 0:
            raise ValueError("El retiro no puede ser negativo")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes")
        self.saldo -= float(monto)

    # mostrar
    def mostrar(self) -> None:
        print(f"Titular: {self._titular} ")
        print(f"Saldo: {self._saldo:.2f} ")

    # repr
    def __repr__(self) -> str:
        return f"CuentaBancaria(titular={self._titular!r}, saldo={self._saldo!r})"
    # str
    def __str__(self) -> str:
        return f"{self._titular} | saldo: {self._saldo:.2f}"
# test
c = CuentaBancaria('Pere Pou', 100)
# print(repr(c))
# print(str(c))
c.mostrar()
c.depositar(50)
# c.mostrar()
# c.retirar(100)
# c.mostrar()

# c2 = CuentaBancaria()
# c2.titular = 'Bruno R'
# c2.saldo = 10
# c2.mostrar()

