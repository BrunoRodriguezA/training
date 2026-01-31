from flask import Flask, render_template, redirect, url_for
from clienteDAO import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma
app = Flask(__name__)
app.config['SECRET_KEY'] = 'llave_secreta'

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
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    # Creamos objetos cliente, inicialmente objetos vacios
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    # valida la información de los campos del formulario
    if cliente_forma.validate_on_submit():
        # llenamos el objeto cliente con los valores del formulario 
        cliente_forma.populate_obj(cliente) # tambien recupera el id oculto del form 
        
        if not cliente.id_cliente:
            # guardamos el nuevo cliente en la base de datos 
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente)
        
    # Redireccionar a la pag de inicio
    return redirect(url_for('inicio'))

@app.route('/eliminar/<int:id>') #localhost:5000/eliminar/1
def eliminar(id):
    cliente = Cliente(id_cliente=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))


@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>') # localhost:5000/editar/1
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForma(obj=cliente)
    # recuperar listado de clientes 
    clientes_db = ClienteDAO.seleccionar()
    
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

if __name__ == "__main__":
    app.run(debug=True)