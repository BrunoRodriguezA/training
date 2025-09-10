from python.poo.udemy.gestor_cursos.Curso import Curso
from numbers import Real


class CursoEnVivo(Curso):
    def __init__(self, titulo:str, duracion_sesion: float, sesiones:int) -> None:
        super().__init__(titulo)
        self.duracion_sesion = duracion_sesion
        self.sesiones  = sesiones

    @property
    def duracion_sesion(self) -> float:
        return self._duracion_sesion

    @duracion_sesion.setter
    def duracion_sesion(self, valor: float) -> None:
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise TypeError('duracion_sesion ha de ser numerico')
        if valor <= 0:
            raise ValueError('duracion_sesion ha de ser >0')
        self._duracion_sesion = float(valor)

    @property
    def sesiones(self) -> int:
        return self._sesiones

    @sesiones.setter
    def sesiones(self, valor: int) -> None:
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise TypeError('sesiones ha de ser numerico')
        if valor <= 0:
            raise ValueError('sesiones ha de ser >0')
        self._sesiones = int(valor)

    def carga_horaria(self) -> float:
        return self._duracion_sesion * self._sesiones
