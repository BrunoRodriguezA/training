import tkinter as tk 
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.configurar_ventana()
        self.configurar_grid()
        
    def configurar_ventana(self):
        self.geometry('600x400')
        self.configure(background='#1d2d44')
        self.title('Manejo de Ventana con POO')
        
    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()