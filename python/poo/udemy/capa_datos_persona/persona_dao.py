from persona import Persona
from conexion import Conexion
from logger_base import log 

class PersonaDAO:
    _SELECT = "SELECT * FROM persona ORDER BY id_persona"
    _INSERT = "INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)"
    _UPDATE = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    _DELETE = "DELETE FROM persona WHERE id_persona = %s"
    
    @classmethod
    def select(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                personas = []
                for registro in  registros: 
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas
        
        # aqui hay que aplicar la poo para poder acceder a los atributos de persona 
        # si lo printeamos no estariamos aplicando la programación orientada a obj
        # Declaramos un cursor propio por si el cursor previo se ha cerrado , esto se maneja mejor con un pool de conexiones 
        
    @classmethod
    def insert(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERT, valores)
                log.debug(f"Persona a insertada: {persona}")
                return cursor.rowcount
        # se ha de aplicar como una transacción, con with            
    
    @classmethod
    def update(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._UPDATE, valores)
                log.debug(f"Persona actualizada: {persona}")
                return cursor.rowcount

    @classmethod
    def delete(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valor = (persona.id_persona,)
                cursor.execute(cls._DELETE, valor)
                log.debug(f"Persona eliminada: {persona}")
                return cursor.rowcount
            # como estamos dentro del contexto del tipo with, no tenemos que hacer commit 

# DAO - DATA ACCESS OBJECT 
# CRUD - CREATE-READ-UPDATE-DELETE        
        
if __name__ == "__main__":
    # # Insertar un registro
    # persona1 = Persona(nombre='Pedro', apellido='Najera', email='pnajera@mail.com')
    # personas_insertadas = PersonaDAO.insert(persona1)
    # log.debug(f"Personas insertadas: {personas_insertadas}")
    
    # # Actualizar un registro 
    # persona1 = Persona(1, 'Juan Carlos', 'Perez', 'cjjuarez@mail.com')
    # personas_actualizadas = PersonaDAO.update(persona1)
    # log.debug(f"Personas actualizadas: {personas_actualizadas}")
    
    # Eliminar un registro
    persona1 = Persona(id_persona=13)
    personas_eliminadas = PersonaDAO.delete(persona1)
    log.debug(f"Personas eliminadas: {personas_eliminadas}")
    
    
    # SELECT objetos
    personas = PersonaDAO().select()
    for persona in personas:
        log.debug(persona)
    
    # print(os.getcwd())