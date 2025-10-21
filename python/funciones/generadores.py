# def generar_lista():
#     return [1,2,3]

# print("con return ")
# for num in generar_lista():
#     print(num )
    
# #  generaror 

# def generador():
#     yield 1
#     yield 1
#     yield 1
    
# print("con yield")
# for num in generador():
#     print(num )    
    
#-----------------------------------------------------------------------------    

# def generarPares(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield (i)

# pares = generarPares(18) # retorna objeto generador 
# print(pares)
# print(next(pares))
# print(next(pares))

# for p in pares:
    # print(p)
    
#-----------------------------------------------------------------------------    
# def leer_archivo(archivo):
#     with open(archivo, "r") as f:
#         for linea in f:
#             yield linea 
            
# lineas = leer_archivo('file.txt')

# # print(next(lineas))
# # print(next(lineas))
# # print(next(lineas))
# # print(next(lineas))

# for l in lineas:
#     print(l)
    
# util para evitar cargar en memoria grandes cantidades de datos que se deban iterar 
# puede generador datos de una fuente externa (un file) 1 a 1 procesarlo y devolverlos bajo demanda 

#-----------------------------------------------------------------------------    

# 2) Fibonacci
def fibo(n):
    a, b = 0, 1 #1,1 # #1,2 #2,3 # 3,5 # 5,8
    for _ in range(n):
        yield a
        a, b = b, a + b   
    

# fib_nums = fibo(6)
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
# print(next(fib_nums))
        
# def fib(n):
#     if n < 0:
#         raise ValueError("error")
#     if n <2:
#         return n 
#     return fib(n-1) + fib(n-2)

# print([fib(i) for i in range(6)])