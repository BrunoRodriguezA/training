import mysql.connector


conn = mysql.connector.connect(
    user='root',
    password='admin',
    database='personas_db',
    host='localhost',
    port='3306'
)   # <- objeto conector 

cur = conn.cursor()
sentencia = "DELETE FROM personas WHERE id=%s"
valores = (5,)
cur.execute(sentencia,valores)
conn.commit()
print("Se ha eliminado el registro")
conn.close()