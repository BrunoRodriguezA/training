#

class Coche:
    def __init__(self,  marca:str, modelo:str, color:str) -> None:
        self._marca = marca # atributo publico
        self._modelo = modelo # atriuto protegido
        self._color = color # atributo privado

    # get y set se usan solo fuera de la clase

    def conducir(self):
        print(f"""Conduciendo el coche: 
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}
        """)

    # @property
    def get_marca(self) -> str:
        return self._marca
    def set_marca(self, marca:str) -> None:
        self._marca = marca

    def get_modelo(self) -> str:
        return self._modelo
    def set_modelo(self, modelo: str) -> None:
        self._modelo = modelo

    def get_color(self) -> str:
        return self._color
    def set_color(self, color:str) -> None:
        self._color = color


# progra principal
if __name__ == "__main__":
    coche1 = Coche('volvo', 'xc40', 'black onyx')
    coche1.conducir()

    # fuera de la clase no deberiamos acceder a los atributos no publicos
    # coche1.marca = 'Toyota'
    # coche1._modelo = 'Yaris'  # esto no es una buena practica
    # coche1.__color = 'Azul' # ignoro la modificación
    # coche1._Coche__color = 'Azul marino' # mala practica
    # coche1.conducir()

    # fuera de la clase no deberiamos acceder a los atributos no publicos
    coche1.set_marca('Toyota')
    coche1.set_modelo('Yaris') # esto no es una buena practica
    coche1.set_color('Azul marino') # ignoro la modificación
    coche1.conducir()