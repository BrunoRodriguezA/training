# Dada una lista de listas de enteros, devolver una lista con los
# cuadrados de los pares, manteniendo el orden de aparición.

def cuadrados_pares(nested: list[list[int]]) -> list[int]:
    return [elemento ** 2 for sublista in nested for elemento in sublista if type(elemento) is int and elemento % 2 == 0]


# elemento (expresion por cada elemento y se añade a la nueva lista)
# primer bucle que itera por cada sublista dentro de nested
# segundo bucle que itera por cada elemento de cada sublista
# condicional para filtrar
