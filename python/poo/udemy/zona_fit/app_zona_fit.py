from clienteDAO import ClienteDAO
from cliente import Cliente

print("Clientes de Zona Fit (GYM)".center(50,"-"))
opcion = None 
while opcion != 5:
    print("""Menu:
          [1] Listar clientes
          [2] Agregar cliente
          [3] Modificar cliente
          [4] Eliminar cliente
          [5] Salir
          """)
    opcion = int(input("Ecribe tu opcion: (1-5): "))
    
    if opcion == 1:
        print("\n*** LISTADO DE CLIENTES ****")
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            print(cliente)
        print()
    elif opcion == 2:
        nombre_var = input("Escribe el nombre: ")
        apellido_var = input("Escribe el apellido: ")
        membresia_var = input("Escribe el membresia: ")
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        ClienteDAO.insertar(cliente)
    elif opcion == 3:
        id_cliente_var = input("Escribe el id: ")
        nombre_var = input("Escribe el nombre: ")
        apellido_var = input("Escribe el apellido: ")
        membresia_var = input("Escribe el membresia: ")
        cliente = Cliente(id_cliente=id_cliente_var,nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        ClienteDAO.actualizar(cliente)
    elif opcion == 4:
        id_cliente_var = input("Escribe el id: ")
        cliente = Cliente(id_cliente=id_cliente_var)
        ClienteDAO.eliminar(cliente)
else:
    print("Salimos del programa")