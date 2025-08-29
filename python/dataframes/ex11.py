# Lee los tres CSV con parse_dates adecuado y valida tipos con info.

import pandas as pd

ventas = pd.read_csv("ventas.csv", parse_dates=['fecha'])
sensores = pd.read_csv("sensores.csv", parse_dates=['ts'])
tickets = pd.read_csv("tickets.csv", parse_dates=['created_at','closed_at'])

print()
print(tickets.info())