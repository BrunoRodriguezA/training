# Palíndromo alfanumérico

def es_palindromo(s:str) -> bool:
    s = s.casefold()
    t = [c for c in s if c.isalnum()]
    return  t == t[::-1]

# uso de casefold() y isalnum() -> mas robusto y general
# list(filter(lambda x: x(condicion), iterable)  -> opcion sensible
