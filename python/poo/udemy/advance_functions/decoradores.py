
def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes')
        resultado = funcion(*args, **kwargs) #llamamos a nuestra funcion, propagamos los parametros 
        print('Despues')
        return resultado
    return wrapper # funciones de orden superior, solo pasamos la referencia pero no se ejecutan 

@decorador
def saludar(nombre):
    print(f"Hola {nombre}")


saludar('Carlos')