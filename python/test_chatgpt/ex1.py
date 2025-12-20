import random

def is_even(n):
    return n & 1 == 0 # bit menos significativo 

# print(is_even(5))
numeros = [n for n in range(10+1)]
for n in numeros:
    print(f"{n} es par {is_even(n)}")
    
    