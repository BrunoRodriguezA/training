from functools import reduce

def cuadrado(x):
    return x ** 2  

print(cuadrado(5))

# Funcion lambda (anonima)
cuadrado_lambda = lambda x: x ** 2
print(cuadrado_lambda(4))

# con map y lambda 
numeros = [1,2,3,4,5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# con filter y lambda 
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# reduce y map 
suma_acumulativa = reduce(lambda x,y: x+y, numeros)
print(suma_acumulativa)


# objetivo, que sean codigos muy compactos pero tambien mas entendible 

