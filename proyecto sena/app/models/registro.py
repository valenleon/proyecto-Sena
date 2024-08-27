from app import db

class Registro(db.Model):
    __tablename__ = 'registro'
    idRegistro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.idUsuario'))
    vigilantes_id = db.Column(db.Integer, db.ForeignKey('vigilante.idVigilante'))
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False) 

    usuarios = db.relationship("Usuario", back_populates="registros")
    vigilantes = db.relationship("Vigilante", back_populates="registros")