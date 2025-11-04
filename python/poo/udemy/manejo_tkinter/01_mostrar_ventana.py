import tkinter as tk 

# creamos una ventana 
ventana = tk.Tk()

# redimenzionar la ventana 
ventana.geometry('600x400')

# modificar titulo 
ventana.title('Nueva ventana')

# redimensionar la ventana 
ventana.resizable(0,0)

#color ventana 
ventana.configure(background='#1d2d44')

# hacemos visible la ventana 
ventana.mainloop()