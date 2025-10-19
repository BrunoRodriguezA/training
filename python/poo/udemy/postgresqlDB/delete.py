import psycopg2

conn = psycopg2.connect(user='postgres', password='admin', dbname='test_db', host='127.0.0.1', port='5432')

try:
    with conn:
        with conn.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            # valores = (7,)
            entrada = input("id_persona a eliminar (separados por coma): ") 
            valores = (tuple(entrada.split(",")), )
            cursor.execute(sentencia, valores) 
            registros_borrados = cursor.rowcount
            print(f"Registros eliminados: {registros_borrados}")
            # for r in registros: print(r)
except Exception as e:
    print(f"Error - {e}, {type(e)}")
finally:
    conn.close()
    
# APRENDIDO: 
    # eliminar un registro de un db con python -> DELETE FROM table WHERE col1=val1 
    # con with no hace falta declarar el conn.commit()
    # eliminar varios registros con una sola instrucción usando tuplas, cursor.execute tambien se puede 