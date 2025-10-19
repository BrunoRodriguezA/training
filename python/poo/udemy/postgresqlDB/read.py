import psycopg2
import pandas as pd 
import pandas.io.sql as sqlio 


# objeto de tipo conexion 
conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')
#print(conexion)

# -----
# cursor = conexion.cursor() # cursor, metodo que permite ejecutar sentencias sql en postgres 
# query = 'SELECT * FROM persona'
# cursor.execute(query)
# registros = cursor.fetchall() # fetchall , recupera todos lso registros de la sentencia ejecutada 

# df = sqlio.read_sql_query(query, conexion)
# -----

## --- CON PANDAS --- ## 
# df_aux = pd.read_sql_query(query, conexion)
# print(df_aux.head())
## -------------------
# print(registros)
# cursor.close()
# conexion.close()


# bloque with, cuando se trabaja con conexiones no se cierra la conexion segun docu, mejor ponerlo dentro de un try finally 
try:
    with conexion:
        with conexion.cursor() as cursor:
            query = 'SELECT * FROM persona WHERE id_persona IN %s' #placeholders 
            # llaves_primarias = ((1,2,3),)
            entrada = input("Proporciona los ids a buscar (separado por comas): ")
            entrada = (tuple(entrada.split(",")),)
            # id_persona = 1  
            # cursor.execute(query)
            cursor.execute(query, entrada)
            registros = cursor.fetchall() # 
            # registro = cursor.fetchone() # solo devuelve un registro 
            for registro in registros:
                print(registro)

except Exception as e:
    print(f"Error - {e}, {type(e)}")
finally:
    conexion.close()

# 265 - leer solo un valor, utilizando placeholders 
# 266 - buscar varios valores de manera dinamica, utilizando tuplas y placeholders 