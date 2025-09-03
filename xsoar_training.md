### sla | sla timer 
    - se puede definir para los tipos de incidente como para los fields
    - se pueden modificar los tiempos de los SLAs en base a distintas condiciones como la severidad 
    
    interaccion con los times, puede ser: 
    - Inicio del timer : se puede iniciar desde el propio playbook a traves de las distintas tareas ejecutadas o mediante scripts (no se inician automaticamente con el inicio del incidente) 
    - Parar del timer: pueden ser parados desde el propio playbook, en una seccion del flujo o desde alguna tarea o script
        Se para cuando el incidente termina (running time) 
    - Pause timer: puede ser pausa/iniciado nuevamente desde el playbook 
        
### indicadores     
    extracted - se extraen usando expresiones regulares o usando builtin commands o de hilo de campos 
        Para manejar el numero de indicadores a extraer podemos definir una lista de exclusion (filtro) 
    
    enriched - recolectados usando reputation command siendo configurado en el tipo de indicador 
        podemos excluir integraciones de la ejecucion de los command reputation para un indicador especifico 
        "Do not use by default" - se puede elegir esta opcion dentro de los settings de la integración 
        
auto-extract & enrichment 
    desde los incidents types - reglas de extraccion, especificando que la extraccion ocurra desde el inicio/creacion de una incidencia o campo especifico para este tipo de incidencia 
    plabooks - auto-extraccion a traves de tasks inputs y outputs 
    manual tasks - manual tasks lanzadas desde la cmd o chats (warrom) 
        
        opciones (extraction/enriched) 
            inline - extraccion se ejecutara y luego empezara/continuara con el flujo de ejecución del playbook (tasks) 
            out of band - no es prioritario, realizara la extraccion pero no interrumpe el flujo de ejecución del playbook
            none - no realiza la extracción 
    
    asociacion de los indicadores o un indicador especifico con los incidentes ?? - se usa comando predefinidos, a  traves de automatización, playbooks o cmd 
    
    veredicto de indicadores - ??
        van por severidad; se puede cambiar el orden 
            malicious, suspicious, good, unknown 
    
indicadores custom 
    se ha de probar bien la expresion regular que se utiliza para la extracción, de tal manera aseguramos una fiablidad en los datos 
    
### bucles (loops)  
    el input ha de ser un array pasad como argumento 
    si se pasa el array a un subplaybook no iterara por cada elemento del array, se ha de especificar en las opciones del playbook 
    builtin - itera hasta que se cumple la condicion (corta el bucle) 
    for-each - itera por cada uno de los elementos del array 

### extend context & quite mode 
    - Extend context, usado para controlar que data y cuanta es mostrada en el context 
        utilizado cuando: 
            Se necesita solo un subset del output 
            comandos que no retornan info al context pero producen un raw-response 
            antes de definir el extend context se ha de probar que dato queremos traer concretamente (apoyandose del dt syntax)
            
    - quite mode, puede aumentar la eficiencia de los playbooks en casos donde se maneja  grandes cantidades de datos
        en quite mode, las tareas no printean los inputs/outputs y tampoco realizan el auto-extract de indicadores. 
        solo muestran logs (errors/warnings)
        se puede habilitar desde las configuraciones avanzadas y a nivel de playbook
         las tareas del playbook heredan el quite mode pero tambien se puede habilitar/deshabilitar especificamente para cada tarea 
### data collection by tasks 
    
### automation scripts 
    usar script helper para montar los scripts 
    testar
     def demisto.args()
        demisto.executeCommand
        
    tableToMarkdown 
    return_results

### field change triggered 
    Scripts que se ejecutan cuando cambia el valor de un campo en un incidente 
    Usados para realizar alguna accion fuera del playbook cuando algun campo se modifica manualmente/automaticamente en tiempo real (cambi en la severidad de una inci, iniciar/pausar/detener campos de tipo timer, validar los valores de un campom)
    Puede evitar tambien que un campo pueda ser editado en absoluto (campos sensibles)
    Mejora la consistencia de datos y asegura que ciertos procesos se cumplan en cuanto un campo sea modificado 

    
### field display script 
    scripts que permiten cambiar dinamicamente como se muestra el valor de un campo en xsoar
        por ejemplo, cambiado los valores dentro de un tipo de incidente dependiendo si es un nuevo incidente o no 
    Permite que los formularios de los incidentes sena mas dinamicos, muestra solo los valores relevantes
    Facilita la toma de decisiones rapida, ya que no satura al analista de opciones innecesarias 

        
### sla trigger scripts 
    Scripts que se ejecutan automaticamente cuando el campo timer (SLA) se incumple 
    Sirver para notificar al owner o soc de que ocurrio un SLA breach (by email)
    Se puede tomar acciones para que el incidente no se quede estancando, escalar serveridad, reasignar la inci a un nuevo analista/owner , avananzar en el playbook para que siga otro path 
    Es una forma de automatizar una respuesta cuan el sla se rompe 
    
        
### Dynamics sections 
    Usados para mostrar data de los incidentes, context y listas de xsoar en los incident layouts 
    Se llenan con el output de scripts 
    tambien se puede mostrar graphical charts con xsoar witgets 

### Post Processing Scripts
    Se configuran en cada incident type y se ejecutan justo antes de que un incidente sea cerrado (manualmente o automaticamente usando el comando colseInvestigation)
    Ejecuta acciones de cierre, se asegura que cierta información requerida este presente, sincronizar datos con sistemas externos como Servicenow
    Se ejecutan independientemente de que si el playbook se ejecuto o no
