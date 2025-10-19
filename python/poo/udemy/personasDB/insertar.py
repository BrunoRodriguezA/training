import mysql.connector


conn = mysql.connector.connect(
    user='root',
    password='admin',
    database='personas_db',
    host='localhost',
    port='3306'
)   # <- objeto conector 


cur = conn.cursor()  # <- objeto cursor
sentencia = "INSERT INTO personas(nombre,apellido,edad) VALUES(%s,%s,%s)" 
valores = ('Victor', 'Ramos', 46)
cur.execute(sentencia, valores)
conn.commit()
conn.close()