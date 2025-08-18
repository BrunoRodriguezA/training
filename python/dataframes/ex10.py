# Selección por rango de fechas
#
# En tickets, filtra incidencias creadas en julio de 2025.
# Pistas: .dt.month == 7, between

import pandas as pd
from sqlalchemy import between

tickets = pd.read_csv("tickets.csv")
aux = pd.read_csv("tickets.csv")

tickets['created_at'] = pd.to_datetime(tickets['created_at'])

print(tickets['created_at'].dtype)
print(aux['created_at'].dtype) #por que en este caso me printea un objecto?

incidents_july = tickets[tickets['created_at'].dt.month == 7]
incidents_july_2 = tickets[tickets['created_at'].dt.month()].between(6,8)
print()

# dudas
    #no entiendo como usar el between en df
    # esta bien usado el dt?
