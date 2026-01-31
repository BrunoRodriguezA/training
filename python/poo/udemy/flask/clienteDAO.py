from logger_base import log
from conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    
    _SELECT = 'SELECT * FROM cliente'
    _INSERT = 'INSERT INTO cliente (nombre, apellido, membresia) VALUES(%s,%s,%s)'
    _UPDATE = "UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s"
    _DELETE = "DELETE FROM cliente WHERE id=%s"
    
    @classmethod
    def seleccionar(cls):
        conn = None 
        try:
            conn = Conexion.obtenerConexion()
            with conn.cursor() as cursor:
                cursor.execute(cls._SELECT)
                clientes = []
                registros = cursor.fetchall()
                for registro in registros:
                    cliente = Cliente(registro[0],registro[1],registro[2],registro[3])
                    clientes.append(cliente)
                return clientes                
        except Exception as e:
            log.debug(f"Ocurrio un error al seleccionar los clientes: {e}, {type(e)}")
        finally:
            if conn is not None:
                Conexion.liberarConexion(conn)
            
    @classmethod
    def insertar(cls, cliente):
        conn = None 
        try:
            conn = Conexion.obtenerConexion()
            with conn.cursor() as cursor:
                valores = (cliente.nombre, cliente.apellido, cliente.membresia)
                cursor.execute(cls._INSERT, valores)
                conn.commit()
                log.debug(f"Cliente a insertar : {cliente}")
                return cursor.rowcount                
        except Exception as e:
            log.debug(f"Ocurrio un error al insertar un cliente: {e}, {type(e)}")
        finally:
            if conn is not None:
                Conexion.liberarConexion(conn)

            
    @classmethod
    def actualizar(cls, cliente):
        conn = None 
        try:
            conn = Conexion.obtenerConexion()
            with conn.cursor() as cursor:
                valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id_cliente)
                cursor.execute(cls._UPDATE, valores)
                conn.commit()
                log.debug(f"Ciente a actualizar : {cliente}")
                return cursor.rowcount                
        except Exception as e:
            log.debug(f"Ocurrio un error al actualizar un cliente: {e}, {type(e)}")
        finally:
            if conn is not None:
                Conexion.liberarConexion(conn)
       
    @classmethod
    def eliminar(cls, cliente):
        conn = None 
        try:
            conn = Conexion.obtenerConexion()
            with conn.cursor() as cursor:
                valores = (cliente.id_cliente,)
                cursor.execute(cls._DELETE, valores)
                conn.commit()
                log.debug(f"Ciente a eliminar : {cliente}")
                return cursor.rowcount                 
        except Exception as e:
            log.debug(f"Ocurrio un error al eliminar un cliente: {e}, {type(e)}")
        finally:
            if conn is not None:
                Conexion.liberarConexion(conn)        
            
                
if __name__ == "__main__":
    
    # c1 = Cliente(id_cliente=4,nombre='Daniel', apellido='Torres', membresia='600')
    # c1 = Cliente(id_cliente=9)
    # c2 = Cliente(nombre='Ivonne', apellido='Lopez', membresia='500')
    # c3 = Cliente(id_cliente=9, nombre='Alexa', apellido='Tellez', membresia='400')
    
    # INSERT 
    # clientes_insertados = ClienteDAO.insertar(c3)
    # log.debug(f"Clientes insertados: {clientes_insertados}")
    
    # UPDATE
    # clientes_actualizados = ClienteDAO.actualizar(c3)
    # log.debug(f"Clientes actualizados: {clientes_actualizados}")
    
    # DELETE
    # clientes_eliminados = ClienteDAO.eliminar(c1)
    # log.debug(f"Clientes eliminados: {clientes_eliminados}")    
    
    # SELECT
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes: print(cliente)
    
    