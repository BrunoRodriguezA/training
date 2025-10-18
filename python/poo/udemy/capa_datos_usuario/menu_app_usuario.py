from logger_base import log
from usuario_dao import UsuarioDAO
from usuario import Usuario

opcion = None

while opcion != 5:
    
    print("""Opciones:
    [1] Listar usuarios
    [2] Agregar usuario
    [3] Modificar usuario
    [4] Eliminar usuario
    [5] Salir
    """)
    
    print("MENU".center(50, "-"))
    opcion = int(input("Escribe tu opción (1-5): "))    

    if opcion == 1:
        for user in UsuarioDAO.select(): log.info(user)
    elif opcion == 2:
        username_var = input("Escribe el username: ")
        password_var = input("Escribe el password: ")
        usuarios_insertados = UsuarioDAO.insert(Usuario(username=username_var, password=password_var))
        log.info(f"Usuarios insertados: {usuarios_insertados}")
    elif opcion == 3:
        id_usuario_var = input("Escribe el id_usuario: ")
        username_var = input("Escribe el username: ")
        password_var = input("Escribe el password: ")
        usuarios_actualizados = UsuarioDAO.update(Usuario(id_usuario=id_usuario_var,username=username_var, password=password_var))
        log.info(f"Usuarios actualizados: {usuarios_actualizados}")
    elif opcion == 4:
        id_usuario_var = input("Escribe el id_usuario: ")
        usuarios_eliminados = UsuarioDAO.delete(Usuario(id_usuario=id_usuario_var))
        log.info(f"Usuarios eliminados: {usuarios_eliminados}")   

else:
    log.info("Salimos del programa")
          