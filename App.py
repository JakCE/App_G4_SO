from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
#18.207.189.64
# MySQL connection
app.config['MYSQL_HOST'] = '18.207.189.64'
app.config['MYSQL_USER'] = 'support'
app.config['MYSQL_PASSWORD'] = 'grupo4password'
app.config['MYSQL_DB'] = 'project_G4'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    #cur = mysql.connection.cursor()
    #cur.execute('SELECT * FROM contacts')
    #data=cur.fetchall()
    return render_template('index.html')#, contacts = data)

@app.route('/add_cliente', methods=['POST'])
def add_cliente():
    if request.method == 'POST': #Define método de envío
        id = request.form['id']
        nombres = request.form['nombres'] # request.form recoge datos de formulario
        apellidos = request.form['apellidos']
        celular = request.form['celular']
        email = request.form['email']
        direccion = request.form['direccion']
        cur = mysql.connection.cursor() #genera conexion DB SQL
        cur.execute('INSERT INTO Cliente (id_cliente, nombres, apellidos, n_celular, email, direccion) VALUES (%s, %s, %s, %s, %s, %s)', 
        (id, nombres, apellidos, celular, email, direccion)) # ejecuta comando SLQ datos recogidos del form
        mysql.connection.commit() # Guarda cambios en DB
        #flash('Contact Added Succesfully')
        return redirect(url_for('Index')) #Redirecciona a pagina Index

@app.route('/add_categoria', methods=['POST'])
def add_categoria():
    if request.method == 'POST': #Define método de envío
        id_cat = request.form['id']
        nombre = request.form['nombre'] # request.form recoge datos de formulario
        descripcion = request.form['descripcion']
        cur = mysql.connection.cursor() #genera conexion DB SQL
        cur.execute('INSERT INTO Categoria (id_categoria, nombre, descripcion) VALUES (%s, %s, %s)', 
        (id_cat, nombre, descripcion)) # ejecuta comando SLQ datos recogidos del form
        mysql.connection.commit() # Guarda cambios en DB
        #flash('Contact Added Succesfully')
        return redirect(url_for('Index')) #Redirecciona a pagina Index
    
@app.route('/add_producto', methods=['POST'])
def add_producto():
    if request.method == 'POST': #Define método de envío
        id_prod = request.form['id']
        descripcion = request.form['descripcion'] # request.form recoge datos de formulario
        precio = request.form['precio']
        marca = request.form['marca']
        stock = request.form['stock']
        id_cat = request.form['categoria']
        cur = mysql.connection.cursor() #genera conexion DB SQL
        cur.execute('INSERT INTO Producto (id_producto, descripcion, precio, marca, stock, id_categoria) VALUES (%s, %s, %s, %s, %s, %s)', 
        (id_prod, descripcion, precio, marca, stock, id_cat)) # ejecuta comando SLQ datos recogidos del form
        mysql.connection.commit() # Guarda cambios en DB
        #flash('Contact Added Succesfully')
        return redirect(url_for('Index')) #Redirecciona a pagina Index

@app.route('/add_venta', methods=['POST'])
def add_venta():
    if request.method == 'POST': #Define método de envío
        id_venta = request.form['id_ven']
        id_prod = request.form['id_prod'] # request.form recoge datos de formulario
        id_cli = request.form['id_cli']
        talla = request.form['talla']
        color = request.form['color']
        cantidad = request.form['cantidad']
        fecha = request.form['fecha']
        monto = request.form['monto']
        cur = mysql.connection.cursor() #genera conexion DB SQL
        cur.execute('INSERT INTO Venta (id_venta, id_producto, id_cliente, talla, color, cantidad, fecha, monto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', 
        (id_venta, id_prod, id_cli, talla, color, cantidad, fecha, monto)) # ejecuta comando SLQ datos recogidos del form
        mysql.connection.commit() # Guarda cambios en DB
        #flash('Contact Added Succesfully')
        return redirect(url_for('Index')) #Redirecciona a pagina Index

@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE contacts
        SET fullname = %s,
            email = %s,
            phone = %s
        WHERE id = %s
        """, (fullname,phone,email,id ))
        mysql.connection.commit()
        flash('Contact updated successfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)