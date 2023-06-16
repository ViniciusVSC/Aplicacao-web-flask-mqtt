from flask import Blueprint, render_template, redirect, url_for, request, flash
from models.cliente.cliente import Cliente
from models.cliente.telefone import Telefone
from models.cliente.endereco import Endereco
from models.db import db


login_bp = Blueprint('login', __name__, template_folder='../views', static_folder="../static/")


@login_bp.route('/index')
def index():
    return render_template('index.html')

@login_bp.route('/login')
def login():
    return render_template('login.html')

@login_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@login_bp.route('/save_cliente', methods=["POST"])
def save_cliente():
    nome = request.form.get("nome", None)
    cpf = request.form.get("cpf", None)
    email = request.form.get("email", None)
    senha = request.form.get("senha", None)
    telefone = request.form.get("telefone", None)
    estado = request.form.get("estado", None)
    municipio = request.form.get("municipio", None)
    bairro = request.form.get("bairro", None)
    rua = request.form.get("rua", None)
    numero = request.form.get("numero", None)
    cep = request.form.get("cep", None)


    cliente = Cliente(nome=nome, cpf=cpf, email=email, senha=senha)
    tel = Telefone(telefone = telefone,cliente_id = cliente.id)
    ende = Endereco(estado = estado, municipio = municipio,bairro=bairro,
                    rua = rua,numero =numero,cep = cep, cliente_id = cliente.id)
    cliente.telefones.append(tel)
    cliente.enderecos.append(ende)
    db.session.add(cliente)
    db.session.commit()


    return redirect(url_for("login.cadastro"))
