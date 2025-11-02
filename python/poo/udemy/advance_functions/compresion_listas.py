# filtrar solo los numeros pares y generar nuevas lista con esos valores 

numeros = range(1,10+1)

pares = []

# sin usar compresion de listas 
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(pares)

# usando compresion de listas 
n_pares = [n**2 for n in numeros if n % 2 == 0]
print(n_pares)