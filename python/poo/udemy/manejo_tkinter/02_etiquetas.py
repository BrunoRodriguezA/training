import tkinter as tk 
from tkinter import ttk

# creamos una ventana 
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(background='#1d2d44')

# creamos etiqueta 
etiqueta = ttk.Label(ventana, text="Saludos")
# publicamos un componente
etiqueta.pack(pady=20)

# cambiar el texto usando el metodo configure 
etiqueta.configure(text='Nos vemos ...')
# cambiar texto con la ayuda de la llave text 
etiqueta['text'] = 'Adios'


# hacemos visible la ventana 
ventana.mainloop()