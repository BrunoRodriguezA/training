import tkinter as tk 
from tkinter import ttk

# creamos una ventana 
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(background='#1d2d44')

# Manejo de grid 
boton1 = ttk.Button(ventana, text='Boton1')
boton2 = ttk.Button(ventana, text='Boton2')
boton3 = ttk.Button(ventana, text='Boton3')

# recomendable utilizar la mayor cantidad de columnas 

# # Publicando de manera horizontal
boton1.grid(row=0, column=0, padx=20, pady=20, ipadx=30, ipady=30)
boton2.grid(row=0, column=1, sticky=tk.SE, ipadx=20, ipady=20)
boton3.grid(row=0, column=2, sticky=tk.NW)

# # Publicando de manera vertical
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=0)
# boton3.grid(row=2, column=0)

#configurar el grid para las columnas 
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=1)
ventana.columnconfigure(2,weight=1)
# configurar el grid para las filas 
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=1)
ventana.rowconfigure(2,weight=1)

# # # Publicando de manera diagonal
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=1)
# boton3.grid(row=2, column=2)

# frame = ventanda dentro de otra 
# un grid dentro de un frame 

# hacemos visible la ventana 
ventana.mainloop()