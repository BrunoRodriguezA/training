import re 

def normalize_spaces(s):
    # quite espacios al inicio y final 
    s = s.strip()
    # Reemplace cualquier grupo de espacios múltiples por un solo espacio.
    s_n = re.sub("\\s+", " ", s)
       
    return s_n


def normalize_spaces_gpt(s):
    # quite espacios al inicio y final 
    # Reemplace cualquier grupo de espacios múltiples por un solo espacio.
    return " ".join(s.split())

s = ' hola    mund o cruel'
print(s.split())
s_n = " ".join(s.split())
print(s_n)
# print(normalize_spaces(s))
# print(normalize_spaces_gpt(s))


