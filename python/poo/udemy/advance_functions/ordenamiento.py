
# sorted(iterable, key=None, reverse=False)

empleado = ['Juan', 'Pedro', 'Maria']

# ordenar lista 
empleado_sorted = sorted(empleado, reverse=False)
print(empleado_sorted)

# ordenar un dict proporcionando un llave 
empleados_dict = [
    {'nombre':'Juan', 'salario':3000},
    {'nombre':'Maria', 'salario':2500},
    {'nombre':'Pedro', 'salario':3500}
]

empleados_dict_sorted = sorted(empleados_dict, key=lambda x: x['salnombreario'])
print(empleados_dict_sorted)