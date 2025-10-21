from typing import Optional
class Cliente:
    
    def __init__(self, id_cliente:Optional[int]=None, nombre:Optional[str]=None, apellido:Optional[str]=None, membresia:Optional[int]=None):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._apellido = apellido
        self._membresia = membresia
        
    @property
    def id_cliente(self) -> Optional[int]:
        return self._id_cliente
    @id_cliente.setter
    def id_cliente(self, value: Optional[int]) -> None:
        self._id_cliente = value
        
    @property
    def nombre(self) -> Optional[str]:
        return self._nombre
    @nombre.setter
    def nombre(self, value: Optional[str]) -> None:
        self._nombre = value
        
    @property
    def apellido(self) -> Optional[str]:
        return self._apellido
    @apellido.setter
    def apellido(self, value: Optional[str]) -> None:
        self._apellido = value
        
    @property
    def membresia(self) -> Optional[str]:
        return self._membresia
    @membresia.setter
    def membresia(self, value: Optional[str]) -> None:
        self._membresia = value
        
    def __str__(self):
        return f"{self.__class__.__name__} {self._id_cliente} {self._nombre} {self._apellido} {self._membresia}"
    
    
    
# definición atributos
    # encapsulamiento 
    # metodo str 
    
if __name__ == "__main__":
    c1 = Cliente(1,'Pep', 'Ocho', '123')
    c2 = Cliente(nombre='Pep',apellido='Ocho', membresia='123')
    # c2 = Cliente(3,'Pere', 'Pou', '456')
    print(c1)
    print(c2)