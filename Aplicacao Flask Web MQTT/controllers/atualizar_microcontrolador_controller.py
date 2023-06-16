from flask import render_template,url_for,request,flash,redirect
from models import db
from models import Microcontrolador
from flask import Blueprint

atualizar_microcontrolador_bp = Blueprint("atualizar_microcontrolador", __name__)

@atualizar_microcontrolador_bp.route("/atualizar_microcontrolador/<int:id>", methods=["GET", "POST"])
def atualizar_microcontrolador(id):
    microcontrolador = Microcontrolador.get_microcontrolador(id)
    url_atualizar = url_for('atualizar_microcontrolador.atualizar_microcontrolador', id=id)

    if request.method == "POST":
        # Obter os dados atualizados do formulário
        nome = request.form['nome']
        tipo = request.form['tipo']

        # ... atualize outros campos conforme necessário

        # Atualizar os dados do cliente no banco de dados
        microcontrolador.nome = nome
        microcontrolador.tipo = tipo
        
        # ... atualize outros campos conforme necessá

# Atualizar o endereço do cliente

        # Realizar o commit para salvar as alterações no banco de dados
        db.session.commit()

        # Redirecionar para uma página de sucesso ou exibir uma mensagem informando que a atualização foi realizada com sucesso
        flash('Microcontrolador atualizado com sucesso!', 'success')
        return redirect(url_for('atualizar_microcontrolador.atualizar_microcontrolador', id=id))

    return render_template("atualizar_microcontrolador.html", microcontrolador=microcontrolador, url_atualizar=url_atualizar)
