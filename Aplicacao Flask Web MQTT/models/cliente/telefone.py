from models.db import db
from models.cliente.cliente import Cliente



class Telefone(db.Model):
    __tablename__ = 'telefones'

    id = db.Column("id", db.Integer(), primary_key=True)
    telefone = db.Column(db.String(20), nullable=False, unique=True)
    cliente_id = db.Column(db.Integer(), db.ForeignKey(Cliente.id))

    def __init__(self, telefone, cliente_id):
        self.telefone = telefone
        self.cliente_id = cliente_id
