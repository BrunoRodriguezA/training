import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', database='test_db', host='127.0.0.1', port="5432")


try: 
    with conexion:
        with conexion.cursor() as cursor:
            query = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s, %s, %s)'
            valores = (
                ('Marcos', 'Cantu', 'mcantu@mail.com'),
                ('Angel', 'Quintana', 'aquintana@mail.com'),
                ('Maria', 'Gonzales', 'mgonzales@mail.com'),
                )
            # cursor.execute(query, valores)
            cursor.executemany(query, valores)
            # conexion.commit() # Al user with, ya no hace falta hacer un commit, se hace automatico
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
except Exception as e:
    print(f"Error - {e}, {type(e)}")
finally:
    conexion.close()

    
# Aprendido:
    # insertar un registro dese python, INSERT INTO table(col1,col2), VALUES(val1,val2)
    # Al usar with, los commit se hacen automaticos 
    # Para obtener num de registros insertados - rowcount
    # executemany, permite insertar varios registros con una sola instrucción usando tuplas 
    # si ocurre un error  se hace un rollback