import tkinter as tk 
from tkinter import ttk

# creamos una ventana 
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(background='#1d2d44')

def mostrar():
    texto = caja_texto.get() # recuperar valor de caja de texto
    print(f"Texto proporcionado: {texto}")
    etiqueta['text'] = texto

# caja texto 
caja_texto = ttk.Entry(ventana, font=('Arial', 15))
caja_texto.pack(pady=20)

# boton 
boton1 = ttk.Button(ventana, text='Enviar', command=mostrar)
boton1.pack(pady=20)

# etiqueta 
etiqueta = ttk.Label(ventana, text=f"Valor inicial")
etiqueta.pack(pady=20)

# hacemos visible la ventana 
ventana.mainloop()