# Calcula el número y el porcentaje de nulos por columna en cada dataset.
import pandas as pd

ventas = pd.read_csv("ventas.csv", parse_dates=['fecha'])
sensores = pd.read_csv("sensores.csv", parse_dates=['ts'])
tickets = pd.read_csv("tickets.csv", parse_dates=['created_at','closed_at'])

####
conteo = ventas.isna().sum()
perct = (ventas.isna().mean() * 100).round(2)


print()