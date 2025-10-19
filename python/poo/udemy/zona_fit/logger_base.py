import logging as log 
from pathlib import Path

#fecha | error lvl | namefile | n_linea |message 
filePath = Path(__file__).parent / 'zona_fit.log'

log.basicConfig(level=log.DEBUG,
                format=('%(asctime)s: %(levelname)s [%(filename)s:%(lineno)2d] - %(message)s'),
                handlers=[
                    log.StreamHandler(),
                    log.FileHandler(filename=filePath, encoding='utf8')],
                datefmt='%I:%M:%S %p'
                )

if __name__ == "__main__":
    log.debug("Mensaje Prueba de conexión")