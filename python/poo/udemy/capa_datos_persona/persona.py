from logger_base import log

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None) -> None:
        self._id_persona = id_persona
        self._nombre = nombre 
        self._apellido = apellido
        self._email = email 
        
    # id_persona
    @property
    def id_persona(self) -> int:
        return self._id_persona
    @id_persona.setter
    def id_persona(self, value:int) -> None:
        self._id_persona = value 
    
    #nombre        
    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, value: str) -> None:
        self._nombre = value
    
    #apellido
    @property
    def apellido(self) -> str:
        return self._apellido
    @apellido.setter
    def apellido(self, value: str) -> None:
        self._apellido = value
        
    # email 
    @property
    def email(self) -> str:
        return self._email
    @email.setter
    def email(self, value: str) -> None:
        self._email = value
    
    def __str__(self) -> str:
        return f"{__class__.__name__}(id_persona={self._id_persona}, nombre={self._nombre}, apellido={self._apellido}, email={self._email})"

if __name__ == "__main__":
    p1 = Persona(1,'Pep', 'Pou', 'ppou@mail.com')
    log.debug(p1)
    # SIMULAR UN INSERT 
    p1 = Persona(nombre='Juan',apellido='Perez', email='jperez@mail.com')
    log.debug(p1)
    # SIMULAR UN DELETE
    p1 = Persona(id_persona=1)
    log.debug(p1)
    # print(p1)
    # print(p1.nombre)


# APRENDIDO:
    # usar Snippets para crear atojos para metodos y propiedades que se autocompleten 
    # Al tener valores por default, se ha de pasar los parametros por nombre