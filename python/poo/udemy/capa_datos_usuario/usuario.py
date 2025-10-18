from typing import Optional

class Usuario:
    def __init__(self, id_usuario: Optional[int]=None, username: Optional[str]=None, password: Optional[str]=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    @property
    def id_usuario(self) -> Optional[int]:
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, value: Optional[int]) -> None:
        self._id_usuario = value
    
    @property
    def username(self) -> Optional[str]:
        return self._username
    @username.setter
    def username(self, value: Optional[str]) -> None:
        self._username = value
    
    @property
    def password(self) -> Optional[str]:
        return self._password
    @password.setter
    def password(self, value: Optional[str]) -> None:
        self._password = value    
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self._id_usuario}, {self._username}, {self._password}"
    
# Responsabilidad crear objetos entidad usuario
if __name__ == "__main__":
    u1 = Usuario(id_usuario=1)
    u2 = Usuario(username="Pep")
    u3 = Usuario(password="***")
