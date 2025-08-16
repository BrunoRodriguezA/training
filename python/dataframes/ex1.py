
import pandas as pd
#Dado un DataFrame de empleados, implementa salario_medio_por_departamento(df) que:
#
# filtre empleados con sueldo > 3000
# agrupe por departamento
# devuelva una Serie con el sueldo medio por departamento (índice = departamento)
# Nota: ordena el índice para pruebas deterministas.


df = pd.DataFrame({
    "nombre": ["Ana","Luis","Juan","Marta","Pedro"],
    "departamento": ["IT","IT","Ventas","Ventas","IT"],
    "sueldo": [3500, 2800, 4000, 2500, 5000]
})


ser = (df.loc[df['sueldo']>3000].groupby('departamento')['sueldo'].mean().sort_index())
ser.name = 'sueldo_medio'
