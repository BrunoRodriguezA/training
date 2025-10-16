import psycopg2 as bd

conn = bd.connect(user='postgres', password='admin', dbname='test_db', host='127.0.0.1', port='5432')

try:
    with conn:
        with conn.cursor() as cursor:
            sentencia = "INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)"
            valores = ('Alex', 'Rojas', 'arojas@mail.com')
            cursor.execute(sentencia, valores)
    
            sentencia = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
            valores = ('Juan', 'Perez', 'jperez@mail.com', 1)
            cursor.execute(sentencia, valores)            
except Exception as e:
    print(f"Ocurrio un Error, se hizo rollback - {e}, {type(e)}")
finally:
    conn.close()
    print("Termina la transacción, se hizo commit en la bd")
    
    
# APRENDIDO: 
   # autocommit=True, no es buena practica, lo normal es con with o commit manual para evitar alterar el estado de la bd 
   # manejo de recursos, con with hacer rollback automaticamente en caso de error 