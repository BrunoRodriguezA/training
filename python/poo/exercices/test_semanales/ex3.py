# Diccionario contador:

lista_nombres = ['pepe', 'fone', 'pepe', 'mario', 'fone', 'fone']

def dict_contador(lista):
    dict_nombres = {}
    for name in lista_nombres:
        dict_nombres[name] = dict_nombres.get(name, 0) + 1 
    return dict_nombres
print(dict_contador(lista_nombres))



# Función con validación:

def dividir(a,b):
    if b == 0:
        raise ValueError('No se puede dividr por 0')
    return a/b 

# List comprehension:
nums = [1, 2, 3, 4, 5]
cuadrados = [n*n for n in nums if n %2 != 0]
print(cuadrados)