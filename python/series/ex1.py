import pandas as pd
from numbers import Real

# ds = pd.Series([2,4,5,5,1])
#print(ds)

lista = ['a',2,1.2,True, [1,2], {'a':1}, pd.Timestamp('2025-08-16')]

# Write a Pandas program to create a Series from a list containing different data types and then filter out elements of a specific type.
s = pd.Series(lista)

only_str = s[s.map(lambda x: isinstance(x,str))]
only_int = s[s.map(lambda x: isinstance(x,Real) and not isinstance(x, bool))]



def filter_by_types(series: pd.Series, typ):
    return series[series.map(lambda x: isinstance(x, typ))]

print(filter_by_types(s,int))


