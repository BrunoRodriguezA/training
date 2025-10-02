#Objetivo: Dada una lista de diccionarios {str:int} , sumar los valores por clave

from collections import Counter

def sumar_por_clave_aux(lista : list[dict[str,float]]) -> dict[str,float]:
    final_dict = {}
    for dicti in lista:
        for k,v in dicti.items():
                final_dict[k] = final_dict.get(k, 0) + v
    return final_dict

entrada = [{"a": 1, "b": 2}, {"b": 3, "c": 4}, {"a": 5}]

def sumar_por_clave(lista):
    c = Counter()
    for d in lista:
        c.update(d)
    return (dict(c))
