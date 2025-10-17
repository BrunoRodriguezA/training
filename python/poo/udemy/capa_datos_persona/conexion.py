import psycopg2 as db 
import logging

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conn = db.connect(user=_USERNAME, password=_PASSWORD, dbname=_DATABASE, host=_HOST, port=_DB_PORT)
    _cursor = _conn.cursor()
    
    @classmethod
    def obtenerConexion(cls):
        return cls._conn
    
    @classmethod
    def obtenerCursor(cls):
        return cls._cursor
    @classmethod
    def cerrar(cls) -> None:
        cls.conn.close()
        
if __name__ == "__main__":
    # c1 = Conexion()
    # cur = c1.obtenerCursor()
    # cur.execute("SELECT * FROM persona")
    # registros = cur.fetchall()
    # print(registros)
    print()
    