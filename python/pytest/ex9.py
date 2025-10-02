# Objetivo: En una cadena, enmascarar números de tarjeta de 16 dígitos
# en formatos: dddddddddddddddd , dddd dddd dddd dddd o dddd-dddd-dddd-dddd . Mantén
# separadores y muestra solo los últimos 4 dígitos

import re

_pat = re.compile(r'(?<!\d)(\d{4}[ -]?\d{4}[ -]?\d{4})([ -]?)(\d{4})(?!\d)')

def enmascarar_tarjetas(s: str) -> str:
    def repl(m: re.Match) -> str:
        # enmascaro todos los bloques de 4 dígitos en g1 y conservo separadores
        masked_g1 = re.sub(r'\d{4}', '****', m.group(1))
        return f'{masked_g1}{m.group(2)}{m.group(3)}'
    return _pat.sub(repl, s)

def enmascarar_tarjetas_aux(s: str) -> str:

    tarjetas = re.findall(r"(?<!\d)(\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4})(?!\d)", s)

    for tarjeta in tarjetas:
        ultimos_digitos = tarjeta[-4:]
        numeros_cifrados = re.sub(r"\d{4}", "****", tarjeta[:-4])
        num_tarjeta_cifrado = f"{numeros_cifrados}{ultimos_digitos}"
        s = re.sub(tarjeta, num_tarjeta_cifrado, s)
    print(s)
    # return  s

texto = "Pago 1234 5678 9012 3456 y 4321-0000-1111-2222 otro 4444444444444444 otro xx1234567890123457yy"
# esp = "Pago **** **** **** 3456 y ****-****-****-2222"
#
print(enmascarar_tarjetas(texto))

# print(re.findall(r"\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}", texto))


