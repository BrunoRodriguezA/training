import tkinter as tk 
from tkinter import ttk
# from clienteDAO import ClienteDAO
from clienteDAO import ClienteDAO

class App(tk.Tk):
    
    _COLOR_VENTANA = "#1d2d44"
    
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()    
        
    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background= App._COLOR_VENTANA)
        self.resizable(0,0)
        
        # Aplicamos estilos 
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam') # preparamos los estilos para el modo oscuro
        self.estilos.configure(self, background=App._COLOR_VENTANA, foreground='white',
                               fieldbackground='black')
    
    
    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
    
    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)', font=('Arial', 15), background=App._COLOR_VENTANA,
                             foreground='white')
        etiqueta.grid(row=0, column=0, columnspan=2, pady=30)
        
    def mostrar_formulario(self):
        ...
        
    def mostrar_tabla(self):
        self.frame_tabla = ttk.Frame(self)
        # definimos estilo de la tabla 
        self.estilos.configure('Treeview', background='black', foreground='white',
                               filedbackground='black', rowheight=20)
        # definimos las columnas 
        columnas = ('Id', 'Nombre', 'Apellido', 'Membresia')
        # creamos el objeto tabla 
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show='headings')
        # agregar los cabeceros 
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.W)
        self.tabla.heading('Apellido', text='Apellido', anchor=tk.W)
        self.tabla.heading('Membresia', text='Membresía', anchor=tk.W)
        
        # Definir las columas 
        self.tabla.column('Id', anchor=tk.CENTER, width=50)
        self.tabla.column('Nombre', anchor=tk.W, width=100)
        self.tabla.column('Apellido', anchor=tk.W, width=100)
        self.tabla.column('Membresia', anchor=tk.W, width=100)
        
        # cargar los datos de la base de datos 
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
                self.tabla.insert(parent='', index=tk.END, values=(cliente.id_cliente, cliente.nombre, 
                                                                   cliente.apellido,cliente.membresia))
        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        
        # publicamos la tabla (dentro del frame tabla)
        self.tabla.grid(row=0,column=0)
        # mostramos el frame de tabla 
        self.frame_tabla.grid(row=1, column=1, padx=20)
        
        
if __name__ == "__main__":
    
    app = App()
    app.mainloop()
        
    