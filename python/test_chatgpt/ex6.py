# has_duplicates(items) devuelve True si hay duplicados,
# False si todos son únicos.
# Ej: [1,2,3] → False, [1,2,2] → True

def has_duplicates(items):
    return any(items.count(i) > 1 for i in items)

items = [1,3,2]
print(has_duplicates(items))


def has_duplicates_gpt(items):
    return len(items) != len(set(items))

print(has_duplicates_gpt(items))