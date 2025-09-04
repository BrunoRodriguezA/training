class Persona:
    contador_personas = 0

    def __init__(self, nombre:str, apellido:str):
        # incrementamos el attr de clase
        Persona.contador_personas += 1

        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f"Persona: {self.id}, {self.nombre}, {self.apellido}")

    @staticmethod
    def get_contador_personas_estatico():
        print('Metodo estatico')
        return Persona.contador_personas

    # forma mas pytonica
    @classmethod
    def get_conta_personas_clase(cls):
        print('Metodo de clase')
        return cls.contador_personas


if __name__  == "__main__":
    p1 = Persona('gerardo', 'Perez')
    p1.mostrar_persona()
    print()
    p2 = Persona('Pepa', 'Pig')
    p2.mostrar_persona()

    print(Persona.contador_personas)
    print(f'contador objetos persona desde obj {p1.contador_personas}')
    print(f'Persona static: {Persona.get_contador_personas_estatico()}')
    print(f'Persona clase: {Persona.get_conta_personas_clase()}')

    # contexto estatico -> no puede acceder al contexto dinamico
    # contexto dinamico  -> puede acceder al contexto estatico

