from models.db import db

class EnderecoEmpresa(db.Model):
    __tablename__ = 'endereco_empresas'

    id = db.Column(db.Integer(), primary_key=True)
    estado = db.Column(db.String(50))
    municipio = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    rua = db.Column(db.String(100))
    numero = db.Column(db.String(20))
    cep = db.Column(db.String(10))
