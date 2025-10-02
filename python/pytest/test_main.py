from ex9 import enmascarar_tarjetas

def test_enmascarar_tarjetas():
    texto = "Pago 1234 5678 9012 3456 y 4321-0000-1111-2222"
    esp = "Pago **** **** **** 3456 y ****-****-****-2222"
    assert enmascarar_tarjetas(texto) == esp
    assert enmascarar_tarjetas("Nada aquí") == "Nada aquí"


