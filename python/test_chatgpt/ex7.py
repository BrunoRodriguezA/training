# Crea safe_int(s, default=None):
# Si s se puede convertir a int, devuelve el int
# Si no, devuelve default
# Ej: "12" → 12, "12a" → None (o el default que pasen)

def safe_int(s, default=None):
    try:
        return int(s)
    except (ValueError, TypeError):
        return default
    
print(safe_int('12a'))
