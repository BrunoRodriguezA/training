# Write a Pandas program to create a Series from a range of dates and assign random numbers as values, then select a subset based on a condition on the index date.

import numpy as np
import pandas as pd

rng = pd.date_range('2025-01-01', periods=20, freq='D')
# print(rng)
np.random.seed(0)

s = pd.Series(np.random.random(len(rng)), index=rng, name='value')

# print(s)

after_10 = s[s.index >= '2025-01-10']
# print(after_10)

weekdays = s[s.index.weekday < 5]
print(weekdays)