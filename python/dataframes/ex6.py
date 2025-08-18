# Selección y orden
#
# Top 10 pedidos por ingreso_neto.
# Pistas: nlargest, sort_values

import pandas as pd
ventas = pd.read_csv("ventas.csv")

ventas['ingreso_bruto'] = ventas['precio'] * ventas['cantidad']
ventas['ingreso_neto'] = ventas['ingreso_bruto'] * (1 - ventas['descuento_pct'].fillna(0))

# ventas = ventas.sort_values(by='ingreso_neto', ascending=False)
top_ten = ventas.nlargest(10, 'ingreso_neto')

# dudas
    # cuando se filtra por segmento o se ordena es mejor creo otro df ? o se puede setear el orignal?
print()