# Filtra ventas por una lista de ciudades y un rango de precios; devuelve conteo e ingreso total.
import pandas as pd
ventas = pd.read_csv("ventas.csv")

ventas = ventas.assign(ingreso_bruto = lambda x: x['precio'] * x['cantidad'],
                       ingreso_neto = lambda x: x['ingreso_bruto'] * (1 - x['descuento_pct'].fillna(0))
                       )
ventas_filtered = ventas[ventas['ciudad'].isin(['Barcelona', 'Madrid']) &  ventas['precio'].between(1, 10, inclusive='both')]

conteo = len(ventas_filtered)
ingreso_total = ventas_filtered['ingreso_neto'].sum()

# opcion 2 (proque me da solo 1 linea)
mask = ventas['ciudad'].isin(['Barcelona', 'Madrid']) & ventas['precio'].between(2, 5, inclusive='both')
ventas_filtered_mask = ventas.loc[mask].copy()
print()