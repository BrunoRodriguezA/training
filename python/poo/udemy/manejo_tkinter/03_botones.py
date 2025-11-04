import tkinter as tk 
from tkinter import ttk

# creamos una ventana 
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(background='#1d2d44')

def saludar(nombre):
    print(f"Saludos {nombre}")

boton1 = ttk.Button(ventana, text='Enviar', command=lambda: saludar('Juan'))  # importante no mandar a llamar el metodo, solo asociar la llamada 
boton1.pack(pady=20)



# hacemos visible la ventana 
ventana.mainloop()