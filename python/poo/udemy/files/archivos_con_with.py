from ManejoArchivos import ManejoArchivos
# with open('prueba.txt', 'r', encoding='utf-8') as file:
with ManejoArchivos('prueba.txt') as file:
    print(file.read())
