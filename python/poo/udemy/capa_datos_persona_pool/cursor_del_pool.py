from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conn = None
        self._cursor = None
        
    def __enter__(self):
        log.debug(f"Inicio del metodo with __enter__")
        self._conn = Conexion.obtenerConexion() # indirenctamente a partir del pool de conexiones 
        self._cursor = self._conn.cursor() # directamente a partir del obj conn obtener el cursor 
        return self._cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug(f"Se ejecuta metodo __exit__")
        if exc_val:
            self._conn.rollback()
            log.error(f"Ocurrio un execpcion: {exc_val}, {exc_type}, {exc_tb}")
        else:
            self._conn.commit()
            log.debug(f"Commit de la transacción")
            
        self._cursor.close()
        Conexion.liberarConexion(self._conn)
        
# APRENDIDO 
    # Creamos una clase encargada de crear una conexion y liberarlas de manera automatica usando el concepto de with (resource manager)
    # Solicitamos objeto conn y cursor
    # Al salir del with, verificamos si hay una execpcion, rollback|commit
    
    
if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug("Dentro del bloque with")
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())
        