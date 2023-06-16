from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.iot.sensor import Sensor
from models.iot.microcontroller import Microcontrolador
from models.iot.atuador import Atuador
from models.db import db

cadastro_iot =  Blueprint('cadastro_iot', __name__, template_folder='./views/cadastro_iot')

@cadastro_iot.route('/cadastro_sensor')
def cadastro_sensor():
    return render_template('/cadastro_iot/cadastro_sensor.html')

@cadastro_iot.route('/cadastro_microcontrolador')
def cadastro_microcontrolador():
    return render_template('/cadastro_iot/cadastro_microcontrolador.html')

@cadastro_iot.route('/cadastro_atuador')
def cadastro_atuador():
    return render_template('/cadastro_iot/cadastro_atuador.html')


@cadastro_iot.route('/save_sensor', methods=["POST"])
def save_sensor():
    nome = request.form.get("nome", None)
    tipo = request.form.get("tipo", None)

    sensor = Sensor(nome=nome, tipo=tipo)

    db.session.add(sensor)
    db.session.commit()

    return redirect(url_for("cadastro_iot.cadastro_sensor"))

@cadastro_iot.route('/save_microcontrolador', methods=["POST"])
def save_microcontrolador():
    nome = request.form.get("nome", None)
    tipo = request.form.get("tipo", None)

    microcontrolador = Microcontrolador(nome=nome, tipo=tipo)

    db.session.add(microcontrolador)
    db.session.commit()

    return redirect(url_for("cadastro_iot.cadastro_microcontrolador"))

@cadastro_iot.route('/save_atuador', methods=["POST"])
def save_atuador():
    nome = request.form.get("nome", None)
    tipo = request.form.get("tipo", None)
    configuracao = request.form.get("configuracao",None)

    atuador = Atuador(nome=nome, tipo=tipo, configuracao=configuracao)

    db.session.add(atuador)
    db.session.commit()

    return redirect(url_for("cadastro_iot.cadastro_atuador"))