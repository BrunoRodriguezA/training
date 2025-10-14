try:
    file = open('prueba.txt', 'w', encoding='UTF-8')
    file.write("información del archivo\n")
    file.write("Adios")
except Exception as e:
    print(e)
finally:
    file.close()
    # file.write("Adios")
    print('End file')

