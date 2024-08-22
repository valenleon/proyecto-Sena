from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    tipousuario_id = db.Column(db.Integer, db.ForeignKey('tipousuario.idTipoUsuario'))
    computador_id = db.Column(db.Integer, db.ForeignKey('computador.idComputador'))

    tipo = db.relationship("TipoUsuario", back_populates="usuarios")
    computadores = db.relationship("Computador", back_populates="usuarios")
    registros = db.relationship("Registro", back_populates="usuarios")