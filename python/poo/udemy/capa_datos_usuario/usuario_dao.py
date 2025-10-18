from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario

class UsuarioDAO:

    _SELECT = "SELECT * FROM usuario"
    _INSERT = "INSERT INTO usuario(username,password) VALUES(%s,%s)"
    _UPDATE = "UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s"
    _DELETE = "DELETE FROM usuario WHERE id_usuario=%s"

    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insert(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f"Usuario a insertar: {usuario}")
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
        
    @classmethod
    def update(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f"Usuario a actualizar: {usuario}")
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._UPDATE, valores)
            return cursor.rowcount
        
    @classmethod
    def delete(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f"Usuario a eliminar: {usuario}")
            valores = (usuario.id_usuario,)
            cursor.execute(cls._DELETE, valores)
            return cursor.rowcount    

if __name__ == "__main__":
    
    # INSERT 
    # u1 = Usuario(username='jperez', password='123')
    # u2 = Usuario(username='kgomez', password='456')
    # u_insertados = UsuarioDAO.insert(u1)
    # log.debug(f"Usuarios insertados: {u_insertados}")
    
    # UPDATE  
    # u1 = Usuario(id_usuario=3, username="jcperez", password='000')
    # u_actualizados = UsuarioDAO.update(u1)
    # log.debug(f"Usuarios actualizados:{u_actualizados}")
    
    #DELETE 
    # u1 = Usuario(id_usuario=5)
    # u_eliminados = UsuarioDAO.delete(u1)
    # log.debug(f"Usuarios eliminados: {u_eliminados}")
    
    # SELECT
    registros = UsuarioDAO.select()
    for r in registros: log.debug(r)
    