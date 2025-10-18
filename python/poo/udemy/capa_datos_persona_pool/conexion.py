from psycopg2 import pool
from logger_base import log
import sys 

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1 
    _MAX_CON = 5
    _pool = None
    

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                      host=cls._HOST, user=cls._USERNAME,
                                                      password=cls._PASSWORD, dbname=cls._DATABASE,
                                                      port=cls._DB_PORT)
                log.debug(f"Creacion del pool exitosa: {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrio un error al obtener el pool: {e}, {type(e)}")
                sys.exit()
        else:
            return cls._pool
    
    @classmethod
    def obtenerConexion(cls):
        conn = cls.obtenerPool().getconn()
        log.debug(f"Conexion obtenida del pool: {conn}")
        return conn
    
    @classmethod
    def liberarConexion(cls,conn):
        cls.obtenerPool().putconn(conn)
        log.debug(f"Regresamos la conexion al pool: {conn}")
        
    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
        
# APRENDIDO:
    # utilizar un pool de conexiones, definir un min y max de pools 
    # a raiz de un pool, obtener obj de tipo conexion 
    # liberar una conexion y cerrar todas las conexiones 
        
if __name__ == "__main__":
    con1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(con1)
    
    con2 = Conexion.obtenerConexion()
    con3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(con3)
    
    con4 = Conexion.obtenerConexion()
    con5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(con5)
    
    con6 = Conexion.obtenerConexion()
    # Conexion.obtenerConexion()
    # Conexion.obtenerCursor()