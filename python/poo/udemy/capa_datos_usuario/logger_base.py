import logging as log 
from pathlib import Path 


file_path = Path(__file__).parent / "capa_datos.log"

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)02d] - %(message)s',
                datefmt="%I:%M:%S %p",
                handlers=[
                    log.FileHandler(file_path,encoding='utf8'),
                    log.StreamHandler()
                ])

if __name__ == "__main__":
    log.debug("Mensaje de Debug")
    log.warning("Mensaje de Debug")
    log.warning("Ménsaje de Debug")