class Persona:
    atributo_clase = 0

    def __init__(self, atributo_instancia) -> None:
        self.atributo_instancia = atributo_instancia

# Programa Princila
if __name__ == "__main__":
    print(f"atributo de clase: {Persona.atributo_clase}")
    # Modificar att de clase
    Persona.atributo_clase = 10
    print(f"atributo de clase: {Persona.atributo_clase}")

    # lo recomendable para acceder a un atributo de clase no lo hagmos desde los objetos si no desde la propia clase
    # tambien se puede acceder desde el objeto pero no es buena practica
    p1 = Persona(15)
    print(f"Attr de clase de persona1: {p1.atributo_clase}")
    print(f"Attr de instancia de persona1: {p1.atributo_instancia}")
    print()
    p2 = Persona(30)
    print(f"Attr de clase de persona2: {p2.atributo_clase}")
    print(f"Attr de instancia de persona2: {p2.atributo_instancia}")