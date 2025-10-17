import logging as log
from pathlib import Path

current_dir = Path.cwd()
# file_path= current_dir / "capa_datos.log" # en vscode el path es la raiz del workspace, o el dir del launch.json 
ruta_archivo = Path(__file__).parent / "capa_datos.log"

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler(ruta_archivo),
                    log.StreamHandler()
                ]
                )

# log.basicConfig()

if __name__ == "__main__":
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critico')

# APRENDIDO 
    # logging para gestionar logs 
    # Por default muestras los niveles de WARNING|ERROR|CRITICAL
    # Se puede indicar el nivel desde los parametros de la config
    # Handler, recurso donde podemos enviar la info consola/archivo
    # Printear fecha, nivel, linea de fichero 