import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__() # constructor de la clase padre tkinter
        
        # configurar ventana 
        self.configurar_ventana()
        # configurar el grid 
        self.configurar_grid()
        # mostrar tabla 
        self.mostrar_tabla()
        
    def configurar_ventana(self):
        self.geometry('600x400')
        self.configure(background='#1d2d44')
        self.title('Manejo de Ventanas con POO')
    
    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        
    def mostrar_tabla(self):
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
        self.tabla = ttk.Treeview(self, columns=columnas, show='headings')        
        
        # cabeceras en la tabla 
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Edad', text='Edad', anchor=tk.W)    
        
        # formato a las columnas
        self.tabla.column('Id', width=80)
        self.tabla.column('Nombre', width=120)
        self.tabla.column('Edad', width=120)            
        
        # cargar datos a la tabla
        datos = ((1,'Alejandra', 25), (2,'Matias', 32))
        
        for persona in datos:
            self.tabla.insert(parent='', index=tk.END, values=persona) # parent valor vacio 

        # agregar scroll bar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        
        # asociar evento select de la tabla 
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_seleccionado)
        
        # Publicamos la tabla (registro 0 columna 0)
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)
        
    def mostrar_seleccionado(self, event):
        print('Ejecutando metodo mostrar_registro_seleccionado')
        elemento_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(elemento_seleccionado)
        persona = elemento['values']
        print(persona)
        showinfo(title='Persona Seleccionada', message=f'Persona: {persona}')
        
if __name__ == '__main__':
    app = App()
    app.mainloop()
        