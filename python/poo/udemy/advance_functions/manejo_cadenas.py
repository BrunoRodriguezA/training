# manejo de cadenas  (parsing)

cadena = 'Hola Mundo'
palabras = cadena.split()
print(palabras)

#buscar con find()
idx = cadena.find('Mundo') # retorna -1 si no encuentra la subcadena
print(idx)

# remplazar replace()
nueva_cadena = cadena.replace('Mundo', 'Amigo')
print(nueva_cadena)

# multiplicacion de cadenas 

cadena = 'Hola '

resultado_multi_cadenas = cadena * 3 
print(resultado_multi_cadenas)

# strip - limpiar una cadena de caracteres al inicio y al final 
cadena = '....Hola Mundo....'
cadena_limpia = cadena.strip('.')

print(cadena_limpia)