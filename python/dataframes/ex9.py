# Conversión de tipos
#
# Convierte prioridad y estado en tickets a Categorical (con orden lógico Alta>Media>Baja y Abierto>En progreso>Cerrado).
# Pistas: astype("category"), CategoricalDtype
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype

tickets = pd.read_csv("tickets.csv")
priority_uniq = tickets['prioridad'].unique()
priority_cat = CategoricalDtype(categories=list(priority_uniq), ordered=True)

print()
# dudas
    # No entiendo como funciona, nunca he visto antes esta función, para que sirve?
    # como aplicarlo en este caso ?


