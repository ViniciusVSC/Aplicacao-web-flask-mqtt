from models.db import db
from models.dispositivo.catalogo import Catalogo
from models.dispositivo.estoque import Estoque
from models.iot.microcontroller import Microcontrolador
from models.iot.atuador import Atuador
from models.iot.sensor import Sensor


class Dispositivo(db.Model):
    __tablename__ = 'dispositivos'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    catalogo_id = db.Column(db.Integer(), db.ForeignKey('catalogos.id'))
    empresa_id = db.Column(db.Integer(), db.ForeignKey('empresas.id'))
    microcontrolador_id = db.Column(db.Integer(), db.ForeignKey('microcontroladores.id'))
    atuador_id = db.Column(db.Integer(), db.ForeignKey('atuadores.id'))
    sensor_id = db.Column(db.Integer(), db.ForeignKey('sensores.id'))

    catalogo = db.relationship('Catalogo', backref='dispositivos', lazy=True)
    empresa = db.relationship('Empresa', backref='dispositivos', lazy=True)
    microcontrolador = db.relationship('Microcontrolador', backref='dispositivos', lazy=True)
    atuador = db.relationship('Atuador', backref='dispositivos', lazy=True)
    sensor = db.relationship('Sensor', backref='dispositivos', lazy=True)
