import math
from decimal import Decimal

## clase float 
# infinito_posi = float('-inf')

## math module 
# infinito_posi = -math.inf


infinito_posi = Decimal('Infinity')
infinito_nega = Decimal('-Infinity')
print(infinito_posi)
print(infinito_nega)



print(f"Es infinito {math.isinf(infinito_posi)}")
print(f"Es infinito {math.isinf(infinito_nega)}")

