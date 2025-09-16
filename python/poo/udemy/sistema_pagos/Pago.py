from abc import ABC, abstractmethod
from numbers import Real
import re

class Pago(ABC):
    def __init__(self, monto:float) -> None:
        self.monto = monto

    @property
    def monto(self) -> float:
        return self._monto
    @monto.setter
    def monto(self, valor:float) -> None:
        if isinstance(valor,bool) or not isinstance(valor,Real):
            raise TypeError("monto ha de ser numerico")
        if valor <=0:
            raise ValueError("monto ha de ser >0")
        self._monto = float(valor)

    @abstractmethod
    def procesar(self) -> str:
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(monto={self._monto!r})"

class PagoTarjeta(Pago):
    def __init__(self, monto:float, numero:str, cvv:str) -> None:
        super().__init__(monto)
        self.numero = numero
        self.cvv = cvv

    # numero
    @property
    def numero(self) -> str:
        return self._numero
    @numero.setter
    def numero(self, valor:str) -> None:
        if not isinstance(valor, str):
            raise TypeError("numero ha de ser una cadena")
        valor = valor.strip().replace(" ", "")
        if not valor:
            raise ValueError("numero no puede ser un campo vacio")
        if not re.fullmatch(r"\d{13,19}", valor):
            raise ValueError("numero ha de tener 13-19 digitos")
        self._numero = str(valor)

    # cvv
    @property
    def cvv(self) -> str:
        return self._cvv
    @cvv.setter
    def cvv(self, valor:str) -> None:
        if not isinstance(valor, str):
            raise TypeError("cvv ha de ser una cadena")
        valor = valor.strip()
        if not valor:
            raise ValueError("cvv no puede ser un camp vacio")
        if len(valor) != 3:
            raise ValueError("cvv ha de ser de 3 digitos")
        if not re.fullmatch(r"\d{3}", valor):
            raise ValueError("cvv ha de ser 3 digitos entre el [0-9]")
        self._cvv = str(valor)

    def procesar(self) -> str:
        mask_card = f"{'*' * (len(self._numero)-4)}{self._numero[-4:]}"
        return f"Se hizo el pago de {self._monto}€, con la tarjeta {mask_card} "


class PagoPaypal(Pago):
    def __init__(self, monto:float, email:str):
        super().__init__(monto)
        self.email = email

    # email
    @property
    def email(self) -> str:
        return self._email
    @email.setter
    def email(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise TypeError("email ha de ser una cadena")
        valor = valor.strip()
        if not valor:
            raise ValueError("email no puede ser un campo vacio")
        #r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not re.fullmatch(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", valor):
            raise ValueError("email no valido")
        self._email = str(valor)

    def procesar(self) -> str:
        return f"Se hizo el pago de {self._monto}€ via Paypal con el email {self._email}"


# polimorfismo
class Checkout:
    def ejecutar(self, pago:Pago) -> str:
        if not isinstance(pago, Pago):
            raise TypeError("Se requiere un Pago")
        return pago.procesar()
#

if __name__ == "__main__":
    p1 = PagoTarjeta(100,'1234567891011', '852')
    p2 = PagoPaypal(50, 'bruno.gnra@gmail.com')
    print(p1)
    print(p2)
    print(p1.procesar())
    print(p2.procesar())
    # opcion A
    ck = Checkout()
    print(ck.ejecutar(PagoPaypal(10, 'pepefone@hotmail.com')))
    # opcion B
    # Con Strategy (cuando hay gateways/servicios externos)

