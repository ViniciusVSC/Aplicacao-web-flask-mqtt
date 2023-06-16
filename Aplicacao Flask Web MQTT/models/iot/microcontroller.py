from models.db import db

class Microcontrolador(db.Model):
    __tablename__ = 'microcontroladores'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)

    def select_microcontroladores():
        microcontroladores = Microcontrolador.query.all()
        return microcontroladores

    def get_microcontrolador(microcontrolador_id):
        microcontrolador = Microcontrolador.query.get(microcontrolador_id)
        return microcontrolador

    def delete_microcontrolador(self):
        db.session.delete(self)
        db.session.commit()