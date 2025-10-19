import mysql.connector 

# creamos la conexion 
personas_db = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password = 'admin',
    database = 'personas_db',
    port= 3306
)

# creamos el cursor en base al conector 
cursor = personas_db.cursor()
cursor.execute("SELECT * FROM PERSONAS")
resultado = cursor.fetchall()

for r in resultado: print(r)