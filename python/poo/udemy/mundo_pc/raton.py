from python.poo.udemy.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca:str, tipo_entrada: str) -> None:
        type(self).contador_ratones += 1
        self.id_raton = type(self).contador_ratones
        super().__init__(marca,tipo_entrada) #llamada al constructor # buena practica

        # primera forma
        # self.marca = marca
        # self.tipo_entrada = tipo_entrada

    def __str__(self) -> str:
        return f"Id: {self.id_raton}, Marca: {self.marca}, Tipo Entrada: {self.tipo_entrada}"

# codigo principal
if __name__ == "__main__":
    r1 = Raton('hp', 'usb')
    r2 = Raton('acer', 'bluethot')
    print(r1)
    print(r2)