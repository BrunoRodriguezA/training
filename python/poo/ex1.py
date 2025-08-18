# Ejercicio 1Permalink
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
from __future__ import annotations
import re
from typing import Optional

class Persona:
    def __init__(self, nombre: Optional[str] = None, edad: Optional[int] = None, dni: Optional[str] = None):
        self._nombre : Optional[str] = None
        self._edad: Optional[int] = None
        self._dni: Optional[str] = None

        if nombre is not None and nombre != "":
            self.nombre = nombre
        if edad is not None and edad != "":
            self.edad = edad
        if dni is not None and dni != "":
            self.dni = dni

    # nombre
    @property
    def nombre(self) -> Optional[str]:
        return self._nombre #self.nombre, recursion infinita

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise ValueError("El nombre ha de ser un string")
        valor = valor.strip()
        if not valor:
            raise ValueError("El nombre no puede estar vacio")

        self._nombre = valor

    # edad
    @property
    def edad(self) -> Optional[int]:
        return self._edad
    @edad.setter
    def edad(self, valor) -> None:
        # consideramos string numericos y enteros
        if isinstance(valor,str):
            if not valor.strip().isdigit():
                raise ValueError("La edad debe ser un entero positivo")
            valor = int(valor)
        if not isinstance(valor, int):
            raise ValueError("La edad debe ser un entero")
        if valor <= 0:
            raise ValueError("La edad deber ser mayor que 0")

        self._edad = valor

    # dni
    @property
    def dni(self) -> Optional[str]:
        return self._dni
    @dni.setter
    def dni(self, valor: str) -> None:
        # que es un string
        if not isinstance(valor, str):
            raise ValueError("El dni deber de ser una cadena")
        valor = valor.strip().upper()
        # validacion basica 8digits + letra
        if not re.fullmatch(r"\d{8}[A-Z]", valor):
            raise ValueError("El DNI debe tener 8 digitis seguidos de un letra")

        self._dni = valor


    def mostrar(self) -> None:
        print(f"Nombre: {self.nombre if self._nombre is not None else '(vacio)'}")
        print(f"edad: {self.edad if self._edad is not None else '(vacio)'}")
        print(f"DNI: {self.dni if self._dni is not None else '(vacio)'}")

    def esMayorEdad(self) -> bool:

        return bool(self._edad is not None and self.edad >=18)

    # representación

    def __str__(self) -> str:
        nom = self._nombre if self._nombre is not None else "?"
        ed = str(self._edad) if self._edad is not None else "?"
        d = self._dni if self._dni is not None else "?"

        return f"Persona(nombre={nom}, edad= {ed}, dni={d})"

# test
p = Persona('Pere Po', 22,'26311903H')
# print(p) # usa str
# p.mostrar()
# print("mayor edad", p.esMayorEdad())

# crea vacia y asigna luego
p2 = Persona()
p2.nombre = "Pau"
p2.edad = "17"
p2.dni = "12345678T"

print(p2)
p2.mostrar()

print(p2.esMayorEdad())

# preguntas,
# por que en el constructor se pone Optional[x]= None y luego en la definicion de los argumentos se vuelve a poner el Optional
# porque se hace un if con "nombre/edad/dni" y luego pones un self.nombre/self.edad/self.dni si antes defines un self._nombre/self._edad/self._dni" ?
# en cada validacion de un argumento tengo que definir un property y su setter? se han de llamar iguar que el argumento ?
# porque se usas el ._ en lo argumentos
# por se usa el -> str o  -> None  o el -> Optional[x]
# los setter no puede hacer un return ?
# porque se hace varias validaciones is not None
# porque se pone un representacion __str__ ( porque una str y no un rep?)
# que buenas practicas hay ? este ha sido un buen ejercicio para empezar?

