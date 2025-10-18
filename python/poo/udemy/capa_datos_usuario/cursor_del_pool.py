from logger_base import log 
from conexion import Conexion


class CursorDelPool():
    def __init__(self):
        self._conn = None 
        self._cursor = None
        
    def __enter__(self):
        log.debug(f"Inicio del método __enter__")
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor 
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        log.debug(f"Inicio del método __exit__")
        if exc_value:
            self._conn.rollback()
            log.error(f"Ocurrio un error en la transacción, rollback aplicado: {exc_type}, {exc_value}, {exc_tb}")
        else:            
            self._conn.commit()
            log.debug(f"Commit de la transacción")
        
        # cierra de cursor y conn manual 
        self._cursor.close()
        Conexion.liberarConexion(self._conn)


if __name__ == "__main__":
    with CursorDelPool() as cursor:
        cursor.execute("SELECT * FROM usuario")
        log.debug(cursor.fetchall())