from typing import List

def añadir_tarea(tareas:List[dict], new_tarea:dict):
    
    for tarea in tareas:
        nombre = tarea.get('titulo')
        if nombre  == new_tarea['titulo']:
            print('Tarea ya existe en la lista')
            break
    else:
        tareas.append(new_tarea)

def marcar_tarea(tareas:List[dict], nombre_tarea:str):
    for tarea in tareas:
        nombre = tarea.get('titulo')
        if nombre  == nombre_tarea:
            tarea['hecha'] = True
            break
    else:
        print('Tarea no encontrada')

def gestor_tareas():
    tareas = []

    while True:
        print("""
            Eliga una opcion:
            1) Añadir tarea
            2) Listar tareas 
            3) Marcar tarea como hecha 
            4) Salir 
            """)
        
        opcion = int(input())
        if opcion ==1:
            nombre = input('Nombre de la tarea: ')
            hecha = False
            new_tarea = {'titulo':nombre, 'hecha': hecha}
            añadir_tarea(tareas, new_tarea)
        
        elif opcion == 2:
            
            for i, tarea in enumerate(tareas, start=1):
                estado = "✅" if tarea["hecha"] else "❌"
                print(f"{i}. {estado} {tarea['titulo']}")
                
        elif opcion == 3:
            idx_tarea = input('Numero de tarea a marcar como hecha: ')
            
            if not idx_tarea.isdigit():
                print("Debes escrbir un numero")
                continue
            
            idx = int(idx_tarea)
            
            if 1 <= idx <= len(tareas):
                tareas[idx-1]['hecha'] = True
            else:
                print("Ese numero no existe")
            
        elif opcion == 4:
            break 

    print('Programa finalizado')
    
gestor_tareas()