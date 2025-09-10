def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

# print(factorial_recursivo(5)) # 120

def fib_rec(n):
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n in (0, 1):         # casos base
        return n
    
    return fib_rec(n-1) + fib_rec(n-2)  # caso recursivo

print(fib_rec(7))