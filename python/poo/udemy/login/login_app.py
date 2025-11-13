import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import showinfo, showerror, showwarning, askokcancel

# creacion del objeto ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva Ventana')
ventana.configure(background='#1d2d44')

#ventana reglones y columnas 
ventana.columnconfigure(0,weight=1)
ventana.rowconfigure(0,weight=1)

# creamos estilo 
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground='white',
                  fieldbackground='black')
estilos.configure('TButton', background='#005f73')
estilos.map('TButton', background=[('active','#0a9396')])

#agregar un frame  (clase - objeto padre)
frame = ttk.Frame(ventana)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(1,weight=3)

#frame titulo 
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
etiqueta.grid(row=0, column=0, columnspan=2)


# usuario 
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

usuario_caja_text = ttk.Entry(frame)
usuario_caja_text.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# password 
password_etiqueta = ttk.Label(frame, text='Password: ')
password_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_caja_text = ttk.Entry(frame, show='*')
password_caja_text.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

frame.grid(row=0, column=0)

# boton
login_botton = ttk.Button(frame, text='Enviar')
login_botton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


def validar(event):
    usuario = usuario_caja_text.get()
    password = password_caja_text.get()

    # usuario = root y password = admin son los valores correctos 
    if usuario == 'root' and password == 'admin':
        showinfo(title='Login', message='Datos correctos!')
    else:
        showwarning(title='Login', message='Datos incorrectos!')
        # askokcancel(title='Login', message='Datos incorrectos!')
#asociar eventos al boton de login 
login_botton.bind('<Return>', validar) # presionar la tecla enter 
login_botton.bind('<Button-1>', validar) # click izquierdo del mouse 

ventana.mainloop()


