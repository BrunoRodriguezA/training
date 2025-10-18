
# sobreescritura de la clase init de la clase object
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # imprimir la info de un objeto en cierto momento
    def __str__(self):
        return f""" Persona
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. mem. = {super.__str__(self)} """
        # importante indicar la referencia para que la clase padre sepa la clase hija con la que se trabaja


p1 = Persona('Ana', 'Botin')
# print(p1) # __str__  se llama automaticamente desde el metodo printi
print(p1.__str__()) # esto es opcional

# si no se sobreescribe,

