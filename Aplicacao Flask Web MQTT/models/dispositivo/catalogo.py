from models.db import db
from models.dispositivo.estoque import Estoque

class Catalogo(db.Model):
    __tablename__ = 'catalogos'

    id = db.Column("id", db.Integer(), primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    preco = db.Column(db.String(200), nullable=False, unique=True)
    descricao = db.Column(db.String(200), nullable=False, unique=True)
    estoque_id = db.Column(db.Integer(), db.ForeignKey('estoques.id'))
