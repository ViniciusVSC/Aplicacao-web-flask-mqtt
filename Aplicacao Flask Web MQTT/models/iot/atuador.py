from models.db import db


class Atuador(db.Model):
    __tablename__ = 'atuadores'

    id = db.Column( db.Integer(), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(30))
    configuracao = db.Column(db.String(100))

    def select_atuadores():
        atuadores = Atuador.query.all()
        return atuadores

    def get_atuador(atuador_id):
        atuador = Atuador.query.get(atuador_id)
        return atuador
    
    def delete_atuador(self):
        db.session.delete(self)
        db.session.commit()
