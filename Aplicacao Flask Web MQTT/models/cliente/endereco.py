from models.db import db
from models.cliente.cliente import Cliente

class Endereco(db.Model):
    __tablename__ = 'enderecos'

    id = db.Column("id",db.Integer(),primary_key=True)
    estado = db.Column(db.String(50), nullable=False, unique=True)
    municipio = db.Column(db.String(100),  nullable=False, unique=True)
    bairro = db.Column(db.String(100),  nullable=False, unique=True)
    rua = db.Column(db.String(100),  nullable=False, unique=True)
    numero = db.Column(db.String(20),  nullable=False, unique=True)
    cep = db.Column(db.String(10),  nullable=False, unique=True)
    cliente_id = db.Column(db.Integer(), db.ForeignKey(Cliente.id))

    def __init__(self, estado, municipio, bairro, rua, numero, cep, cliente_id):
        self.estado = estado
        self.municipio = municipio
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.cep = cep
        self.cliente_id = cliente_id