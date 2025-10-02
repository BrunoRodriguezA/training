# Objetivo: Partir una lista en sublistas de tamaño k . Si k<1 , lanza ValueError

from typing import List, Sequence

def partir_en_trozos(seq:list, k:int) -> list[list]:
    if k <1:
        raise ValueError
    return [seq[i:i+k] for i in range(0,len(seq),k)]

