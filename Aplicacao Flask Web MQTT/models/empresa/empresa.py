from models.db import db
from models.empresa.endereco_empresa import EnderecoEmpresa

class Empresa(db.Model):
    __tablename__ = 'empresas'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(50))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    cnpj = db.Column(db.String(14))
    endereco_empresa_id = db.Column(db.Integer(), db.ForeignKey('endereco_empresas.id'))

    endereco_empresa = db.relationship('EnderecoEmpresa', backref='empresas')
