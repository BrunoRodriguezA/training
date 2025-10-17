import psycopg2 as bd

conn = bd.connect(user='postgres', password='admin', dbname='test_db', host='127.0.0.1', port='5432')

try:
    conn.autocommit = False # True, no es buena practica, lo normal es con with o commit manual 
    cursor = conn.cursor()
    sentencia = "INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)"
    valores = ('Carlos', 'Lara', 'clara@mail.com')
    cursor.execute(sentencia, valores)
    
    sentencia = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)
    
    conn.commit()
    print("Termina la transacción, se hizo commit")
    
except Exception as e:
    conn.rollback()
    print(f"Ocurrio un Error, se hizo rollback - {e}, {type(e)}")
finally:
    conn.close()
    
# APRENDIDO: 
   # autocommit=True, no es buena practica, lo normal es con with o commit manual para evitar alterar el estado de la bd 