# Devolver un diccionario con el conteo de vocales sin acentos:
# a,e,i,o,u (ignora todo lo demás)
import unicodedata


#helper , normalizar acentos

def _strip_accents(s:str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFD", s)
                   if unicodedata.category(ch) != "Mn")

# unicode - codigos de categoria
# Mn = "Marca sin espacios"


def contar_vocales(s:str) -> dict[str,int]:
    v_dict = dict.fromkeys("aeiou", 0)

    for ch in _strip_accents(s).casefold():
        if ch in v_dict:
            v_dict[ch] += 1
    return v_dict

