class Aritmetica:
    def __init__(self, operando1:float=None, operando2:float=None) -> None:
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self) -> float:
        return self.operando1 + self.operando2

    def restar(self) -> float:
        return self.operando1 - self.operando2

    def multiplicar(self) -> float:
        return self.operando1 * self.operando2

    def dividir(self) -> float:
        return self.operando1/self.operando2

if __name__ == "__main__":

    a1 = Aritmetica(5,7)
    print(a1.sumar())
    print(a1.restar())
    print(a1.multiplicar())
    print(a1.dividir())
    print()

    a2 = Aritmetica(12,16)
    print(a2.sumar())
    print(a2.restar())
    print(a2.multiplicar())
    print(a2.dividir())
    print()

    # flexibilidad sobre los constructores en python
    # iniciando los parametros con None, podemos pasar de manera opcional los valores a nuestros parametros
    a3 = Aritmetica(7)
    a3.operando2= 9
    print(a3.sumar())
    print()

    a4 = Aritmetica()
    a4.operando1 = 2
    a4.operando2 = 8
    print(a4.sumar())
    print()

    # a5 = Aritmetica(operando1=3, operando2=4)
    a5 = Aritmetica(operando2=4, operando1=3)
    print(a5.sumar())