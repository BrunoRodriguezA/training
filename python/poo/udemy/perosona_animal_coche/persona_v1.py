# definicion de una clase
class Persona:
    def __init__(self, nombre: str, apellido: str) -> None:
        # comunmente se llama igual atributo y parametro
        self.nombre = nombre
        self.apellido = apellido

    # def inicializar_persona(self, nombre:str, apellido:str):
    #     self.nombre = nombre
    #     self.apellido = apellido

    def mostrar_persona(self):
        print(f"Persona(Nombre={self.nombre}, Apellido={self.apellido})")
        print(f"Dir. mem self: {id(self)}")
        print(f"Dir. mem hex self: {hex(id(self))}")

# creacion objetos
if __name__ == "__main__":
    p1 = Persona('Pep', 'Guardiola')
    # print(p.nombre)
    # print(p.apellido)
    p1.mostrar_persona()
    print()
    p2 = Persona('Jamón', 'Serrano')
    p2.mostrar_persona()
    print(id(p2))
