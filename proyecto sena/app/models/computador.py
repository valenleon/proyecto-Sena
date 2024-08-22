from app import db 

class Computador(db.Model):
    __tablename__ = 'computador'
    idComputador = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(255), nullable=False)
    perisferico_id = db.Column(db.Integer, db.ForeignKey('perisferico.idPerisferico'))

    usuarios = db.relationship("Usuario", back_populates="computadores")
    perisfericos = db.relationship("Perisferico", back_populates="computadores")
