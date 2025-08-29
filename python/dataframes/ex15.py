# En tickets, saca value_counts de prioridad y su versión normalizada en %.

import pandas as pd

tickets = pd.read_csv('tickets.csv')
priori = tickets['prioridad'].value_counts()
pct = (tickets['prioridad'].value_counts(normalize=True)*100).round(1)

# ¿version normalizada ?
print()