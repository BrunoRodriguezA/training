# En ventas, crea ingreso_bruto y ingreso_neto y calcula total y media.

import pandas as pd

ventas = pd.read_csv("ventas.csv")

ventas = ventas.assign(ingreso_bruto = lambda x: x['precio'] * x['cantidad'],
                       ingreso_neto = lambda  x: x['ingreso_bruto'] * (1 - x['descuento_pct'].fillna(0)))

# ingreso_total = ventas['ingreso_neto'].sum()
# ingreso_media = ventas['ingreso_neto'].mean()
res = ventas['ingreso_neto'].agg(total="sum", media="mean")

print()