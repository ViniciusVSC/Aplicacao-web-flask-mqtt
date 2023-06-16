from flask import render_template,url_for,request,flash,redirect
from models import db
from models import Atuador
from flask import Blueprint

atualizar_atuador_bp = Blueprint("atualizar_atuador", __name__)

@atualizar_atuador_bp.route("/atualizar_microcontrolador/<int:id>", methods=["GET", "POST"])
def atualizar_atuador(id):
    atuador = Atuador.get_atuador(id)
    url_atualizar = url_for('atualizar_atuador.atualizar_atuador', id=id)

    if request.method == "POST":
        # Obter os dados atualizados do formulário
        nome = request.form['nome']
        tipo = request.form['tipo']
        configuracao = request.form['configuracao']

        # ... atualize outros campos conforme necessário

        # Atualizar os dados do cliente no banco de dados
        atuador.nome = nome
        atuador.tipo = tipo
        atuador.configuracao = configuracao
        
        # ... atualize outros campos conforme necessá

# Atualizar o endereço do cliente

        # Realizar o commit para salvar as alterações no banco de dados
        db.session.commit()

        # Redirecionar para uma página de sucesso ou exibir uma mensagem informando que a atualização foi realizada com sucesso
        flash('Atuador atualizado com sucesso!', 'success')
        return redirect(url_for('atualizar_atuador.atualizar_atuador', id=id))

    return render_template("atualizar_atuador.html", atuador=atuador, url_atualizar=url_atualizar)
