# Objetivo: Generar el acrónimo de una frase tomando la primera letra de
# cada palabra alfabética.

import re


def acronimo(frase:str) -> str:
    return "".join(ch[0].upper() for ch in (frase.split()))


# considerar ignorar articulos y preposiciones

STOPWORDS = {"de","del","la","el","y","a","en","para","por","con","los","las","un","una","unos","unas","al","lo"}

def acronimo_aux(frase:str) -> str:
    palabras = re.findall(r"[^\W\d_]+", frase)
    return "".join(p[0].upper() for p in palabras if p.casefold() not in STOPWORDS)
