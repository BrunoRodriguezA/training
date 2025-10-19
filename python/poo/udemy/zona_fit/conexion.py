import sys 
from logger_base import log 
from mysql.connector import pooling, Error


class Conexion:
    _DB_CONFIG = {
        "host" : 'localhost',
        "username" : 'root',
        "password" : 'admin',
        "database" : 'personas_db',
        "port" : '3306',
        }
    
    _HOST = 'localhost'
    _USERNAME = 'root'
    _PASSWORD = 'admin'
    _DATABASE  = 'personas_db'
    _DB_PORT = '3306'
    _POOL_SIZE = 5
    _POOL_NAME = 'zona_fit_pool'
    _pool = None
    
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                # cls._pool = pooling.MySQLConnectionPool(pool_name=cls._POOL_NAME, pool_size=cls._POOL_SIZE, **cls._DB_CONFIG)
                cls._pool = pooling.MySQLConnectionPool(pool_name=cls._POOL_NAME, pool_size=cls._POOL_SIZE,
                                                        username=cls._USERNAME, password=cls._PASSWORD,
                                                        database=cls._DATABASE, host=cls._HOST,
                                                        port=cls._DB_PORT)
                # log.debug(f"Poolname: {cls._pool.pool_name}")
                # log.debug(f"Poolsize: {cls._pool.pool_size}")
                return cls._pool
            except Error as e:
                log.debug(f"Ocurrio un error al obtener el pool: {e}, {type(e)}")
        else:
            return cls._pool
        
    @classmethod
    def obtenerConexion(cls):
        try:
            conn = cls.obtenerPool().get_connection()
            return conn
        except Exception as e:
            log.debug(f"Error al obtener la conexión: {e}, {type(e)}")
            sys.exit()
            
    @classmethod
    def obtenerCursor(cls):
        try:
            cursor = cls.obtenerConexion().cursor()
            return cursor
        except Exception as e:
            log.debug(f"Error al obtener el cursor: {e}, {type(e)}")
            sys.exit()
            
    @classmethod
    def liberarConexion(cls, conn):
        conn.close()
        log.debug(f"Conexion devuelta al pool")
        
if __name__ == "__main__":
    con1 = Conexion.obtenerConexion()
    # conn = Conexion.obtenerConexion()
    # cursor = conn.cursor()
    # pool = Conexion.obtenerPool()
    print(con1)
    Conexion.liberarConexion(con1)