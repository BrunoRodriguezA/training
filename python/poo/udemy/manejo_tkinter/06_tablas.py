import tkinter as tk 
from tkinter import ttk
from tkinter.messagebox import showinfo

# crear ventana 

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(background='#1d2d44')
ventana.title('Manejo de tabla')

#configure el grid 
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=0)

# Definir un estilo 
estilos = ttk.Style()
estilos.theme_use('clam') # prepara el manejo de tema oscuro
estilos.configure('Treeview', background='black',
                  foreground='white',
                  fieldbackground='black',
                  rowheight=30
                  )

estilos.map('Treeview', background=[('selected', '#3a86ff')])

# definir columnas 
columnas = ('Id', 'Nombre', 'Edad')

# componente de tabla 
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')

# cabeceras en la tabla 
tabla.heading('Id', text='Id', anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre', anchor=tk.W)
tabla.heading('Edad', text='Edad', anchor=tk.W)

# formato a las columnas
tabla.column('Id', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)

# cargar datos a la tabla
datos = ((1,'Alejandra', 25), (2,'Matias', 32))
#datos = ((1,'Alejandra', 25), (2,'Matias', 32)) + ((1,'Alejandra', 25), (2,'Matias', 32)) + ((1,'Alejandra', 25), (2,'Matias', 32)) + ((1,'Alejandra', 25), (2,'Matias', 32)) + ((1,'Alejandra', 25), (2,'Matias', 32)) + ((1,'Alejandra', 25), (2,'Matias', 32)) + ((1,'Alejandra', 25), (2,'Matias', 32)) + ((1,'Alejandra', 25), (2,'Matias', 32)) + ((1,'Alejandra', 25), (2,'Matias', 32))

for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona) # parent valor vacio 

# agregar scroll bar
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky=tk.NS)


# Mostrar seleccionado 
def mostrar_seleccionado(evento):
    print('Ejecutando metodo mostrar_registro_seleccionado')
    elemento_seleccionado = tabla.selection()[0]
    elemento = tabla.item(elemento_seleccionado)
    persona = elemento['values']
    print(persona)
    showinfo(title='Persona Seleccionada', message=f'Persona: {persona}')

# asociar evento select de la tabla 
tabla.bind('<<TreeviewSelect>>', mostrar_seleccionado)


# Publicamos la tabla (registro 0 columna 0)
tabla.grid(row=0, column=0, sticky=tk.NSEW)

# 
ventana.mainloop()