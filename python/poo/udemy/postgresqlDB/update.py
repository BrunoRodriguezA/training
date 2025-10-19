import psycopg2

conexion = psycopg2.connect(user="postgres", password="admin", dbname="test_db", port="5432", host="127.0.0.1")

try: 
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan', 'Perez', 'jperez@mail.com', 1),
                ('Ivonne', 'Gutierrez', 'igutierrez@mail.com', 2),
                )
            # cursor.execute(sentencia, valores)
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f"Registros actualizados: {registros_actualizados}")
except Exception as e:
    print(f"Error - {e}, {type(e)}")
finally:
    conexion.close()

# Aprendido:
    # actualizar una tabla de python usando placeholders -> UPDATE table SET col1=val1, col2=val2 
    # insertar varios reginstros con una sola instrucción usando tuplas 