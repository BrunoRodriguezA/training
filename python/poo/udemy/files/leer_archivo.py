file = open('prueba.txt', 'r', encoding='UTF-8')
## Leer todo el archivo
# print(file.read())

## Leer algunos caracteres
# print(file.read(5))

## leer lineas completas
# print(file.readline())
# print(file.readline())

## iterar por cada una de las lineas
# for line in file:
    # print(line)

## leer todas las lineas
# print(file.readlines())
# print(file.readlines()[0])
# print(file.readlines()[2])

## abrimos un nuevo archivo
#
file2 = open('copia.txt', 'w', encoding='UTF-8')
file2.write(file.read())
file.close()
file2.close()
