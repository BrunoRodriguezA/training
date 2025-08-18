# En ventas, crea ingreso_bruto = precio * cantidad y ingreso_neto = ingreso_bruto * (1 - descuento_pct.fillna(0)).
import pandas as pd
ventas = pd.read_csv("ventas.csv")

# columnas directas
# ventas['ingreso_bruto'] = ventas['precio'] * ventas['cantidad']
# ventas['ingreso_neto'] = ventas['ingreso_bruto'] * (1 - ventas['descuento_pct'].fillna(0))

# con .asssign (se crea otro dataframe y se usa lambda)
new_ventas = ventas.assign(ingreso_bruto=lambda x: x['precio'] * x['cantidad'],
                           ingreso_neto=lambda x: x['ingreso_bruto'] * (1 - x['descuento_pct'].fillna(0)))

print()

# dudas?
    # cuando usar el assign en vez de crear las columnas directamente
    # siempre al usar assign se ha de crear otro dataframe ? no se puede aplicar los cambios en el mismo?

##
    # assign devuelve un copia
    # si queremos  conservar si a de reasignar