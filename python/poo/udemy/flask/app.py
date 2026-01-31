from flask import Flask, render_template
from clienteDAO import ClienteDAO
app = Flask(__name__)

titulo_app = 'Zona Fit (GYM)'

@app.route('/')  # url http://localhost:5000/
@app.route('/index.html')  # url http://localhost:5000/index.html 

# MODELO MVC - MODELO-CONTROLADOR-VISTA 
# CONTROLADOR app.py - request management
# MODELO cliente.py - datos 
# VISTA index.html - plantilla html 

def inicio():
    app.logger.debug('Entramos al path de inicio /')
    # Recuperamos los clientes de la BD
    clientes_db = ClienteDAO.seleccionar() # modelo 
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db)

if __name__ == "__main__":
    app.run(debug=True)