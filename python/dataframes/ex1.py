# Lee cada CSV y muestra head(), shape, info(), describe(include="all").
import pandas as pd

ventas  = pd.read_csv("ventas.csv")
tickets  = pd.read_csv("tickets.csv")
sensores  = pd.read_csv("sensores.csv")

print(ventas.head(n=5))
print(f"filas={tickets.shape[0]}; columnas={tickets.shape[1]}")
print(sensores.info())
print(ventas.describe(include="all"))

# dudas
    # diferencia entre una serie y un df, que es cada cosa?
