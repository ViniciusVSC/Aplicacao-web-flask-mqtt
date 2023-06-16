from models.db import db
from datetime import datetime

class Leitura(db.Model):
    __tablename__ = 'leituras'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    message = db.Column(db.String(1000), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.now, nullable=False)


    def select_leituras():
        leituras = Leitura.query.all()
        return leituras
    
    def get_leitura(leitura_id):
        leitura = Leitura.query.get(leitura_id)
        return leitura