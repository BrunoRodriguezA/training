import mysql.connector


conn = mysql.connector.connect(
    user='root',
    password='admin',
    database='personas_db',
    host='localhost',
    port='3306'
)   # <- objeto conector 


cur = conn.cursor()  # <- objeto cursor
sentencia = "UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s"
valores = ('Victoria', 'Flores', 45, 5)
cur.execute(sentencia, valores)
conn.commit()
print("Se ha modificado la info.")
conn.close()