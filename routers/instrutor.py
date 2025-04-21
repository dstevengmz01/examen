from flask import render_template, request
from models.sena import NombreSena
from models.intructor import NombreIntructor
from app import app
import random
import string

from correo import enviar_correo_asincrono

@app.route("/agregarinstructor/", methods=['GET', 'POST'])
def agregar_instructor():
    try:
        mensaje = None
        estado = False
        senas = NombreSena.objects()

        if request.method == 'POST':
            datos = request.json
            nombre = datos.get('nombrecompleto')
            correo = datos.get('correoelectronico')
            sena_id = datos.get('sena')
            sena_ref = NombreSena.objects(id=sena_id).first()
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            if sena_ref:
                nuevo_instructor = NombreIntructor(
                    nombrecompleto=nombre,
                    correoelectronico=correo,
                    centro=sena_ref
                )
                nuevo_instructor.set_password(password)
                nuevo_instructor.save()
                correo_destino = nuevo_instructor.correoelectronico
                asunto = "Contraseña de la App "
                mensaje = f"Su contraseña es: {password} su correo es: {correo}"
                enviar_correo_asincrono(correo_destino, asunto, mensaje)
                estado = True
                mensaje = "Instructor agregado correctamente. La contraseña ha sido enviada al correo."
            else:
                mensaje = "Centro SENA no encontrado"
        else:
            mensaje = "Método no permitido"
    except Exception as e:
        mensaje = f"Error: {str(e)}"
        print("EXCEPCIÓN:", mensaje)

    return render_template('agregarinstructor.html', estado=estado, mensaje=mensaje, senas=senas)
