from python.poo.udemy.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Monitor:
    contador_monitores = 0

    def __init__(self, marca: str, tamanio: int) -> None:
        type(self).contador_monitores += 1
        self.id_monitor = type(self).contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self) -> str:
        return f"ID: {self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tamanio}"

if __name__ == "__main__":
    m1 = Monitor('Philips', 25)
    m2 = Monitor('AOC', 30)
    print(m1)
    print(m2)