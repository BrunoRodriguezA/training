# Write a Pandas program to convert a Panda module Series to Python list and it's type.
import pandas as pd

s = pd.Series(data=[1,2,3,4], name='datos')
s_list = s.to_list()

print(s)
print(type(s))

print(s_list)
print(type(s_list))