from models.db import db

class Sensor(db.Model):
    __tablename__ = 'sensores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)

    def select_sensores():
        sensores = Sensor.query.all()
        return sensores

    def get_sensor(sensor_id):
        sensor = Sensor.query.get(sensor_id)
        return sensor

    def delete_sensor(self):
        db.session.delete(self)
        db.session.commit()