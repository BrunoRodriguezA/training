# Dada una lista con posibles repetidos, devolver una nueva lista
# con los elementos únicos en su primer orden de aparición

# version consiza (elementos hasheables)
def unicos_en_orden(seq:list) -> list:
    return list(dict.fromkeys(seq))

# version considerando no hasheables
def unicos_en_orden_nohash(seq:list) -> list:
    out = []
    for ch in seq:
        if ch not in out:
            out.append(ch)
    return out