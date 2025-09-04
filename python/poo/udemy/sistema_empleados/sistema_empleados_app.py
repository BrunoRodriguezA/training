from python.poo.udemy.sistema_empleados.empleado import Empleado
from python.poo.udemy.sistema_empleados.empresa import Empresa

print('*** Sistema de empleados ***')

# crear instancia empresa

empresa1 = Empresa('Golbal mentoring')

#contratar alguos empleados
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('Maria', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')


# obtener el total de objetos de tipo empleado
print(f"Total de Empleados: {Empleado.obtener_total_empleados()}")

# obtener numero de empleados en el departamentos de ventas
print(f"Empleados en el departamento de Ventas: {empresa1.obtener_numero_empleados_por_departamento('Ventas')}")

# mostrar todos los empleados de la empresa1
empresa1.obtener_total_empleados()
