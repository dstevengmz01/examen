from flask import request,render_template,jsonify,redirect,url_for,session,flash
from models.programa import NombrePrograma
from app import app




@app.route("/agregarprograma/",methods=['GET', 'POST'])
def addPrograma():
    # if 'instructor_id' not in session:
    #     flash('Debes iniciar sesión para realizar esta acción', 'warning')
    #     return redirect(url_for('login'))
    try:
        mensaje=None
        estado=False
        if request.method=='POST':
            datos=request.get_json(force=True)
            genero=NombrePrograma(**datos)
            genero.save()
            estado=True
            mensaje="Sena Agregado correctamente"
        else:
            mensaje="No permitido"
    except Exception as error:
        mensaje=str(error)
    return render_template('agregarprograma.html',estado=estado,mensaje=mensaje)