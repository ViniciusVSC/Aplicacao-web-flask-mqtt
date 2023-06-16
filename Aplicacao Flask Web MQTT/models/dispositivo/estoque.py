from models.db import db

class Estoque(db.Model):
    __tablename__ = 'estoques'

    id = db.Column("id", db.Integer(), primary_key=True, autoincrement=True)
    quantidade = db.Column(db.Integer(), nullable=False, unique=True)
