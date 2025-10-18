import sys 
from logger_base import log 
from psycopg2 import pool

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = '127.0.0.1'
    _DB_PORT = '5432'
    _MIN_CONN = 1
    _MAX_CONN = 5
    _pool = None

    # crear el pool 
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(minconn=cls._MIN_CONN, maxconn=cls._MAX_CONN,
                                                    user=cls._USERNAME, password=cls._PASSWORD,
                                                    dbname=cls._DATABASE, host=cls._HOST,
                                                    port=cls._DB_PORT)
                log.debug(f"Creacion del pool exitosa: {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrio un error al obtener el pool de conexiónes: {e}, {type(e)}")
                sys.exit()
        else:
            return cls._pool
        
    # obetener una conexion 
    @classmethod
    def obtenerConexion(cls):
        try:
            conn = cls.obtenerPool().getconn()
            log.debug(f"Conexion obtenida correctamente: {conn}")
            return conn
        except Exception as e:
            log.error(f"Ocurrio un error al obtener la conexión: {e}, {type(e)}")
            sys.exit()
            
    # liberar conexion
    @classmethod
    def liberarConexion(cls, conn):
        cls.obtenerPool().putconn(conn)
        log.debug(f"Regresamos la conexión al pool: {conn}")
            
    # cerrar conexiones
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug(f"Se han cerrado todas las conexiones")
            
if __name__ == "__main__":
    c1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(c1)
    c2 = Conexion.obtenerConexion()
    Conexion.liberarConexion(c2)
    # c3 = Conexion.obtenerConexion()
    # c4 = Conexion.obtenerConexion()
    # c5 = Conexion.obtenerConexion()
    # c6 = Conexion.obtenerConexion()
    