def funcion(secuencia):
    lista = [secuencia[0]]

    for e in secuencia[1:]:
        aux = lista[len(lista)-1]
        if e != lista[len(lista) -1]:
            lista.append((e))
        print()


    return lista

funcion("aA7577hhhA")