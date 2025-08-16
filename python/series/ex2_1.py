# Write a Pandas program to convert a Series containing mixed numeric types to a Python list and then filter out non-integer values.
import pandas as pd
from numbers import Real

s = pd.Series([1,2.1,-1,2.0,0], name='datos')
lst = s.to_list()

insts_only = [x for x in lst if isinstance(x,Real) and  float(x).is_integer()]
print(insts_only)

# NOTAS
# al tener una serie de solo enteros pandas unifica los tipos numericos en dytpe=float64, se upcastean a float
# bool es un subtipo de int en python
