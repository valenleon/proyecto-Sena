from app import db

class Vigilante(db.Model):
    __tablename__ = 'vigilante'
    idVigilante = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)

    registros = db.relationship("Registro", back_populates="vigilantes")