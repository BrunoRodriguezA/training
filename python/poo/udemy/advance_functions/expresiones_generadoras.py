# crea un objeto generador 
generador =  (x**2 for x in range(0,10) if x % 2 == 0)

print(generador)


print(next(generador))
print(next(generador))

# for c in generador:
#     print(c)