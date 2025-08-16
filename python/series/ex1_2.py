import numpy as np
import pandas as pd

# Write a Pandas program to create a Series with a custom index from a NumPy array and then reorder the series based on the index in descending order.

arr = np.array([10,20,30,40])
idx = ['d','b','a','c']

s = pd.Series(data=arr,index=idx)

print(s)
s_desc = s.sort_index(ascending=False)
print(s_desc)