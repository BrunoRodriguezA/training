import psycopg2 as db 
from logger_base import log
import sys 

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conn = None
    _cursor = None
    
    @classmethod
    def obtenerConexion(cls):
        if cls._conn is None:
            try:
                cls._conn = db.connect(user=cls._USERNAME, password=cls._PASSWORD, dbname=cls._DATABASE, host=cls._HOST, port=cls._DB_PORT)
                log.debug(f"Conexión exitosa: {cls._conn}")
                return cls._conn
            except Exception as e:
                log.error(f"Ocurrio una excepción al obtener la conexión: {e}, {type(e)}")
                sys.exit()
        else: 
            return cls._conn
    
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f"Se abrio correctamente el cursor: {cls._cursor}")
                return cls._cursor
            except Exception as e:
                log.error(f"Ocurrio una excepción al obtener el cursor: {e}, {type(e)}")
                sys.exit()
        else:
            return cls._cursor
        
    @classmethod
    def cerrar(cls) -> None:
        if cls._conn:
            cls._conn.close()
        
# APRENDIDO:
    # inicializar las varibles de conexion con non 
    # utilizar try y excep y el manejo de logs 
    # si hay un error al nivel de conexion lo mejor es terminar el programa , sys.exit()         
        
if __name__ == "__main__":
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()