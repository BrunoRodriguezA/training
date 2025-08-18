# Conversión de tipos
#
# Convierte prioridad y estado en tickets a Categorical (con orden lógico Alta>Media>Baja y Abierto>En progreso>Cerrado).
# Pistas: astype("category"), CategoricalDtype
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype

tickets = pd.read_csv("tickets.csv")

prio_type = CategoricalDtype(categories=['Alta', 'Media', 'Baja'], ordered=True)
estado_type = CategoricalDtype(categories=['Abierto', 'En progreso', 'Cerrado'], ordered=True)

tickets['prioridad'] = tickets['prioridad'].astype(prio_type)
tickets['estado'] = tickets['estado'].astype(estado_type)

tickets_sorted = tickets.sort_values(["prioridad", 'created_at'], ascending=[True, False])

print()
# dudas
    # No entiendo como funciona, nunca he visto antes esta función, para que sirve?
    # como aplicarlo en este caso ?


