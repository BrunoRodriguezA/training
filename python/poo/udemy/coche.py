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


    @property # metodo get de manera mas pythonica
    def marca(self) -> str:
        return self._marca

    @marca.setter
    def marca(self, marca:str) -> None:
        self._marca = marca

    @property
    def modelo(self) -> str:
        return self._modelo
    @modelo.setter
    def modelo(self, modelo: str) -> None:
        self._modelo = modelo

    @property
    def color(self) -> str:
        return self._color
    @color.setter
    def color(self, color:str) -> None:
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
    coche1.marca = 'Toyota'
    coche1.modelo = 'Yaris' # esto no es una buena practica
    coche1.color = 'Azul marino' # ignoro la modificación
    # intentar agregar un nuevo atributo
    setattr(coche1, 'nuevo_atributo', 'valor nuevo atributo') # agregar un atributo desde fuera solo para el propio objeto
    coche1.nuevo_att2 = 'Valor nuevo atributo 2'
    coche1.conducir()
    print(coche1.__dict__)

    print(coche1.nuevo_atributo)
    print(coche1.nuevo_att2)

    coche2 = Coche('Opel', 'Moka', 'Blanco')
    coche2.conducir()
    print(coche2.__dict__)
    # print(coche2.nuevo_atributo)
    # print(coche2.nuevo_att2)

    # # atribut de marca del coche
    # print(coche1.marca)
    # coche1.marca = 'Toyota3'
    # print(coche1.marca)

    # malas practicar, crear atributos desde fuera de manera dinamica #dinamismo de python
