from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.iot.atuador import Atuador
from models.iot.microcontroller import Microcontrolador
from models.iot.sensor import Sensor
from models.db import db

listar_dispositivos_bp = Blueprint('listar_dispositivos', __name__, template_folder='./views/lista_iot')

@listar_dispositivos_bp.route("/listar_sensores")
def listar_sensores():
    sensores = Sensor.select_sensores()
    return render_template("/lista_iot/listar_sensor.html", sensores=sensores)

@listar_dispositivos_bp.route("/listar_microcontroladores")
def listar_microcontroladores():
    microcontroladores = Microcontrolador.select_microcontroladores()
    return render_template("/lista_iot/listar_microcontrolador.html", microcontroladores=microcontroladores)

@listar_dispositivos_bp.route("/listar_atuadores")
def listar_atuadores():
    atuadores = Atuador.select_atuadores()
    return render_template("/lista_iot/listar_atuador.html", atuadores=atuadores)


@listar_dispositivos_bp.route("/excluir_sensor/<int:id>", methods=["POST"])
def excluir_sensor(id):
    sensor = Sensor.query.get(id)
    if sensor:
        
        sensor.delete_sensor()

        # Realizar o commit para salvar as alterações no banco de dados
        db.session.commit()

        flash('Sensor excluído com sucesso!', 'success')
    else:
        flash('Sensor não encontrado!', 'error')

    return redirect(url_for('listar_dispositivos.listar_sensores'))

@listar_dispositivos_bp.route("/excluir_microcontrolador/<int:id>", methods=["POST"])
def excluir_microcontrolador(id):
    microcontrolador = Microcontrolador.query.get(id)
    if microcontrolador:
        
        microcontrolador.delete_microcontrolador()

        # Realizar o commit para salvar as alterações no banco de dados
        db.session.commit()

        flash('Microcontrolador excluído com sucesso!', 'success')
    else:
        flash('Microcontrolador não encontrado!', 'error')

    return redirect(url_for('listar_dispositivos.listar_microcontroladores'))

@listar_dispositivos_bp.route("/excluir_atuador/<int:id>", methods=["POST"])
def excluir_atuador(id):
    atuador = Atuador.query.get(id)
    if atuador:
        
        atuador.delete_atuador()

        # Realizar o commit para salvar as alterações no banco de dados
        db.session.commit()

        flash('Atuador excluído com sucesso!', 'success')
    else:
        flash('Atuador não encontrado!', 'error')

    return redirect(url_for('listar_dispositivos.listar_atuadores'))
