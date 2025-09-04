class Aritmetica:
    def __init__(self, operando1:float=None, operando2:float=None) -> None:
        self._operando1 = operando1
        self._operando2 = operando2



    def sumar(self) -> float:
        return self._operando1 + self._operando2

    def restar(self) -> float:
        return self._operando1 - self._operando2

    def multiplicar(self) -> float:
        return self._operando1 * self._operando2

    def dividir(self) -> float:
        return self._operando1/self._operando2

    # Encapsulamiento
    # operand1
    @property
    def operando1(self) -> float:
        return self._operando1
    @operando1.setter
    def operando1(self, valor: float) -> None:
        # if isinstance(valor, bool) or not isinstance(valor,(int,float)):
        #     raise ValueError(f'Operando1 ha de ser numerico')
        self._operando1 = float(valor)

    # operando2
    @property
    def operando2(self) -> float:
        return self._operando2
    @operando2.setter
    def operando2(self, valor:float) -> None:
        # if isinstance(valor, bool) or not isinstance(valor,(int,float)):
        #     raise TypeError(f'Operando2 ha de ser numerico')
        self._operando2 = float(valor)

if __name__ == "__main__":
    a1 = Aritmetica(5,7)
    print(a1.operando1)
    print(a1.operando2)

    print(a1.sumar())
    print(a1.restar())
    print()
    a1.operando1 = 9
    a1.operando2 = 15

    print(a1.sumar())
    print(a1.restar())

    # setattr(a1, 'operando3', 5)
    # print(f"Atributos del objeto: {a1.__dict__}")
    # print(a1.multiplicar())
    #
    # a2 = Aritmetica(operando1=12, operando2=16)
    # print(a2.sumar())
    # print(a2.restar())
    # print(f"Atributos del objeto: {a2.__dict__}")
