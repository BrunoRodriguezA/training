class Empleado:
    contador_empleado = 0

    def __init__(self, nombre:str, departamento:str) -> None:
        self.nombre = nombre
        self.departamento = departamento
        Empleado.contador_empleado += 1
        self.id = Empleado.contador_empleado

    @classmethod
    def obtener_total_empleados(cls) -> int:
        return cls.contador_empleado