from models.db import db



class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)

    telefones = db.relationship("Telefone", backref="clientes", lazy=True)
    enderecos = db.relationship("Endereco", backref="clientes", lazy=True)

    def save_cliente(nome, cpf, email, senha, telefone):
        cliente = Cliente(nome=nome, cpf=cpf, email=email, senha=senha)
        telefone = Telefone(telefone=telefone, id_cliente=cliente.id)
        endereco = Endereco(endereco=endereco, id_cliente=id_cliente)
        cliente.telefones.append(telefone)
        cliente.enderecos.append(endereco)
        db.session.add(cliente)
        db.session.commit()

    def select_clientes():
        clientes = Cliente.query.all()
        return clientes

    def get_cliente(cliente_id):
        cliente = Cliente.query.get(cliente_id)
        return cliente

    def delete_cliente(self):
        db.session.delete(self)
        db.session.commit()
