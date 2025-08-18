# En ventas, asegura que fecha sea datetime y ordénalo por fecha.
import pandas as pd

ventas = pd.read_csv("ventas.csv")
ventas['fecha'] = pd.to_datetime(ventas['fecha'])
ventas_sorted = ventas.sort_values(by="fecha")

print()