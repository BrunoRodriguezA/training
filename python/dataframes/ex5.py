# Valores faltantes
#
# Cuenta nulos por columna en ventas y sensores.
# Pistas: isna().sum()

import pandas as pd
ventas = pd.read_csv("ventas.csv")
sensores = pd.read_csv("sensores.csv")

ventas_nulos = ventas.isna().sum()
sensores_nulos = sensores.isna().sum()

# dudas
    # que hace isna() que devuelve, se puede usar solo ? con que fin ?
    # diferencia entre el isna() y dropna()
    # isna(), engloba valores NaN y celdas vacias ?