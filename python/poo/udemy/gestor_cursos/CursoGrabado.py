from python.poo.udemy.gestor_cursos.Curso import Curso
from numbers import Real

class CursoGrabado(Curso):
    def __init__(self, titulo:str, horas_video:float) -> None:
        super().__init__(titulo)
        self.horas_video = horas_video

    @property
    def horas_video(self) -> float:
        return self._horas_video
    @horas_video.setter
    def horas_video(self, valor:float) -> None:
        if isinstance(valor, bool) or not isinstance(valor,Real):
            raise TypeError('horas_video ha de ser numerico')
        if valor <= 0:
            raise ValueError('horas_video ha de ser >0')
        self._horas_video = float(valor)

    def carga_horaria(self) -> float:
        return self._horas_video
