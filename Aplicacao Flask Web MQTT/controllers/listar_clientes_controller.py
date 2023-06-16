from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.cliente.cliente import Cliente
from models.cliente.telefone import Telefone
from models.cliente.endereco import Endereco
from models import db

listar_clientes_bp = Blueprint('listar_clientes', __name__, template_folder='./views')

@listar_clientes_bp.route("/listar_clientes")
def listar_clientes():
    clientes = Cliente.select_clientes()
    return render_template("listar_clientes.html", clientes=clientes)


@listar_clientes_bp.route("/excluir_cliente/<int:id>", methods=["POST"])
def excluir_cliente(id):
    cliente = Cliente.query.get(id)
    if cliente:
        # Excluir os telefones relacionados ao cliente
        for telefone in cliente.telefones:
            db.session.delete(telefone)

        # Excluir os endereços relacionados ao cliente
        for endereco in cliente.enderecos:
            db.session.delete(endereco)

        # Excluir o cliente
        cliente.delete_cliente()

        # Realizar o commit para salvar as alterações no banco de dados
        db.session.commit()

        flash('Cliente excluído com sucesso!', 'success')
    else:
        flash('Cliente não encontrado!', 'error')

    return redirect(url_for('listar_clientes.listar_clientes'))
