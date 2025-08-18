# Filtros simples
# Filtra pedidos de la ciudad “Madrid” y canal “web”. ¿Cuántos son? ¿ingreso_neto total?
# Pistas: máscaras booleanas, len, sum

import pandas as pd
ventas = pd.read_csv("ventas.csv")

ventas['ingreso_total'] = ventas['precio'] * ventas['cantidad']
ventas['ingreso_neto'] = ventas['ingreso_total'] * (1 - ventas['descuento_pct'].fillna(0))

# mascaras boolenas
pedidos_madrid = ventas['ciudad'] == "Madrid"
canal_web = ventas['canal'] == "web"

ventas = ventas[pedidos_madrid]
ventas = ventas[canal_web]

# mask = (ventas['ciudad'].eq("Madrid")) & (ventas['canal'].eq("web"))
# ventas_mad_web = ventas.loc[mask].copy()

total_ventas = len(ventas)
ingreso_neto_total = ventas['ingreso_neto'].sum()

#dudas
    # cuando usar el isin?
    # que son las mascaras booleanas ?
    #  df_filter = df[df['valor'] > 30 ] , este formato que hace ? podrias explicarmelo
    # como deducir cuando te piden una columna nueva en el df o un dato aparte??, en este caso entendi que totalventas y ingreso neto son datos individuales que no hace falta meterlos en el df
