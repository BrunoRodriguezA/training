# ¿Cuántas categorías y productos únicos hay en ventas? ¿Cuántos dispositivos en sensores?
# Pistas: nunique, unique

import pandas as pd
ventas = pd.read_csv("ventas.csv")
sensores = pd.read_csv("sensores.csv")

# nunique evalua por eje  axis = 0 = indice ; axis = 1 = columnas
# unique evalua por columna df['x'].unique()

cat_unicos = ventas['categoria'].nunique()
prod_unicos = ventas['producto'].nunique()
dev_unicos = sensores['device_id'].nunique()

# dudas
    # me puedes explicar mejor en que casos usar nunique() y unique(), cual es la diferencia?
    # cuando usar drop_duplicates, value_counts , set? en este ejercicio me servirian ?