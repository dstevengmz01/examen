from flask import request,render_template,jsonify,redirect,url_for,session,flash
from models.sena import NombreSena
from app import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/principal/')
def principal():
    return render_template('principal.html')


@app.route("/agregarsena/",methods=['GET', 'POST'])
def addGenero():
    if 'instructor_id' not in session:
        flash('Debes iniciar sesión para realizar esta acción', 'warning')
        return redirect(url_for('login'))
    try:
        mensaje=None
        estado=False
        if request.method=='POST':
            datos=request.get_json(force=True)
            genero=NombreSena(**datos)
            genero.save()
            estado=True
            mensaje="Sena Agregado correctamente"
        else:
            mensaje="No permitido"
    except Exception as error:
        mensaje=str(error)
    return render_template('agregarsena.html',estado=estado,mensaje=mensaje)