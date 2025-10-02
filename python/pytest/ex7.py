# Objetivo: Devolver la longitud de la racha (run) más larga del mismo
# carácter contiguo
from itertools import groupby

def racha_mas_larga(s:str) -> int:
    if not s:
        return 0

    max_run = run = 1
    # si hay mas de un caracter, entrada en el bucle
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            run += 1
        else:
            max_run = max(max_run, run)
            run = 1

    return max(max_run,run)


def racha_mas_larga_aux(s:str) -> int:
    # eliminamos vacios
    if not s:
        return 0
    # primer ch ya cuenta como racha de 1
    racha_maxima = racha = 1

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            racha += 1
        else:
            racha_maxima = max(racha_maxima, racha)
            racha = 1

    # recoge la ultima racha
    return max(racha_maxima, racha)