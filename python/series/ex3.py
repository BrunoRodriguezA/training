# Write a Pandas program to create a Series from a dictionary with duplicate values and then remove duplicates.
import pandas as pd

s_dict = {
    'a' : 1,
    'b': 2,
    'c': 3,
    'd': 3
}

# s = pd.Series(data=s_dict)
# print(s)
# s_sin_dups = s.drop_duplicates(keep='first')
# print(s_sin_dups)

def dict_to_series(dict_values: dict):
    s = pd.Series(data=dict_values)
    s_sin_dups = s.drop_duplicates(keep='first')
    return s_sin_dups

print(dict_to_series(s_dict))