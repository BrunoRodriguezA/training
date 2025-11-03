from pathlib import Path

nombre_file = Path(__file__).parent / 'miarchivo.txt'

try:
    with open(nombre_file, 'x') as archivo:
        archivo.write('hola')
except FileExistsError as e:
    print(f"El nombre del fichero {nombre_file}, ya existe")
    print(f"Ocurrio un error: {e}, {type(e)}")