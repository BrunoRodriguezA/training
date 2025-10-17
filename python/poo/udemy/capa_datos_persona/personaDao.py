from persona import Persona
from conexion import Conexion


class PersonaDao:
    _SELECT = "SELECT * FROM persona"
    _INSERT = "INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)"
    _UPDATE = "UPDATE persona SET nombre=%s, apellido=%s, email=%s"
    _DELETE = "DELETE FROM persona WHERE id_persona = %s"
    
    @classmethod
    def select(cls):
        cursor = Conexion.obtenerCursor()
        cursor.execute(cls._SELECT)
        registros = cursor.fetchall()
        return registros
    
    @classmethod
    def insert(cls, persona):
        cursor = Conexion.obtenerCursor()
        valores = (persona.nombre, persona.apellido, persona.email)
        cursor.execute(cls._INSERT, valores)
        registros_insertados = cursor.rowcount
        print(f"Registros insertados: {registros_insertados}")        
    
    @classmethod
    def update(cls, persona):
        cursor = Conexion.obtenerCursor()
        valores = (persona.nombre, persona.apellido, persona.email)
        cursor.execute(cls._UPDATE)
        registros_actualizados = cursor.rowcount
        print(f"Registros actualizados: {registros_actualizados}")

    @classmethod
    def delete(cls, persona):
        cursor = Conexion.obtenerCursor()
        valor = (persona.id_persona,)
        cursor.execute(cls._DELETE, valor)
        registros_eliminados = cursor.rowcount
        print(f"Registros eliminados: {registros_eliminados}")

        
if __name__ == "__main__":
    p1 = Persona(1,'Pep', 'Pou', 'ppou@email.com')
    pdao = PersonaDao()
    print(pdao.select())