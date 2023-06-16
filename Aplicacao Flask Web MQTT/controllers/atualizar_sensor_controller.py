from flask import render_template,url_for,request,flash,redirect
from models import db
from models import Sensor
from flask import Blueprint

atualizar_sensor_bp = Blueprint("atualizar_sensor", __name__)

@atualizar_sensor_bp.route("/atualizar_sensor/<int:id>", methods=["GET", "POST"])
def atualizar_sensor(id):
    sensor = Sensor.get_sensor(id)
    url_atualizar = url_for('atualizar_sensor.atualizar_sensor', id=id)

    if request.method == "POST":
        # Obter os dados atualizados do formulário
        nome = request.form['nome']
        tipo = request.form['tipo']

        # ... atualize outros campos conforme necessário

        # Atualizar os dados do cliente no banco de dados
        sensor.nome = nome
        sensor.tipo = tipo
        
        # ... atualize outros campos conforme necessá

# Atualizar o endereço do cliente

        # Realizar o commit para salvar as alterações no banco de dados
        db.session.commit()

        # Redirecionar para uma página de sucesso ou exibir uma mensagem informando que a atualização foi realizada com sucesso
        flash('Sensor atualizado com sucesso!', 'success')
        return redirect(url_for('atualizar_sensor.atualizar_sensor', id=id))

    return render_template("atualizar_sensor.html", sensor=sensor, url_atualizar=url_atualizar)
