import random
# multiplos de 3 

# for i in range(1,21):
#     if i % 3 == 0:
#         print(i)
        
# listas y filtros 

nums = [3, 10, -2, 7, 7, 4]
new  = [n for n in nums if n >5]
# print(new)

# contador de palabras 

texto = 'papito mio cuanto te   extraño de '
conteo = len(texto.split())
# print(conteo)

# adivina el numero 
def guess():
    cont = 1
    num = random.randint(1,20)
    
    for _ in range(1,6):
        numero = int(input("Adivina el numero: "))
        if numero == num:
            print(f"Adivinaste, el numero era {num}")
            break 
        elif numero < num:
            print("Mas alto")
        else:
            print("Mas bajo ")
    else:
        print('Se acabaron los intentos')
        
guess()