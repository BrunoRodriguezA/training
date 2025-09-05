from python.poo.udemy.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self, marca: str, tipo_entrada: str) -> None:
        type(self).contador_teclado += 1
        self.id_teclado = type(self).contador_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f"ID: {self.id_teclado}, Marca: {self.marca}, Tipo Entrada: {self.tipo_entrada}"


if __name__ == "__main__":
    t1 = Teclado('Acer', 'usb')
    t2 = Teclado('Samsung', 'bluethot')
    print(t1)
    print(t2)