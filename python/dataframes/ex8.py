# Value counts
#
# En tickets, cuenta incidencias por prioridad y proporciones.
# Pistas: value_counts(normalize=True)

import pandas as pd
tickets = pd.read_csv("tickets.csv")

incidents_by_priority = tickets['prioridad'].value_counts(normalize=False)
incidents_by_prop = tickets['prioridad'].value_counts(normalize=True)

# dudas
    # a que te refieres por prioridad y proporciones, estas pidiendo dos datos distintos ?
    # el normalize que hace exactamente y en que casos aplicarlo ?