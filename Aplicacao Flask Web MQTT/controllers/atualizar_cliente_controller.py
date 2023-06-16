from flask import render_template,url_for,request,flash,redirect
from models import db
from models import Cliente
from flask import Blueprint

atualizar_cliente_bp = Blueprint("atualizar_cliente", __name__)

@atualizar_cliente_bp.route("/atualizar_cliente/<int:id>", methods=["GET", "POST"])
def atualizar_cliente(id):
    cliente = Cliente.get_cliente(id)
    url_atualizar = url_for('atualizar_cliente.atualizar_cliente', id=id)

    if request.method == "POST":
        # Obter os dados atualizados do formulário
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']
        estado = request.form['estado']
        municipio = request.form['municipio']
        bairro = request.form['bairro']
        rua = request.form['rua']
        numero = request.form['numero']
        cep = request.form['cep']

        # ... atualize outros campos conforme necessário

        # Atualizar os dados do cliente no banco de dados
        cliente.nome = nome
        cliente.cpf = cpf
        cliente.email = email
        cliente.senha = senha
        
        # ... atualize outros campos conforme necessário
        cliente.telefones[0].telefone = telefone

# Atualizar o endereço do cliente
        cliente.enderecos[0].estado = estado
        cliente.enderecos[0].municipio = municipio
        cliente.enderecos[0].bairro = bairro
        cliente.enderecos[0].rua = rua
        cliente.enderecos[0].numero = numero
        cliente.enderecos[0].cep = cep

        # Realizar o commit para salvar as alterações no banco de dados
        db.session.commit()

        # Redirecionar para uma página de sucesso ou exibir uma mensagem informando que a atualização foi realizada com sucesso
        flash('Cliente atualizado com sucesso!', 'success')
        return redirect(url_for('atualizar_cliente.atualizar_cliente', id=id))

    return render_template("atualizar_cliente.html", cliente=cliente, url_atualizar=url_atualizar)
