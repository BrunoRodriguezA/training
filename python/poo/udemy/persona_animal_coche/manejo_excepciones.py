from NumerosIdenticosException import NumerosIdenticosException

result = None
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))

    if a == b:
        raise NumerosIdenticosException("Numeros identicos")
    result = a/b
except ZeroDivisionError as e:
    print(f"ZeroDivsionError - Ocurrio un error: {e}, {type(e)}")
except TypeError as e:
    print(f"TypeError - Ocurrio un error: {e}, {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrio un error: {e}, {type(e)}")
else:
    print(f"No se arrojo ninguna excepción")
finally:
    print(f"Ejecucion del bloque finally")

print(result)
