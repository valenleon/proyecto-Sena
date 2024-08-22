from app import db

class TipoUsuario (db.Model):
    __tablename__ = 'tipousuario'
    idTipoUsuario = db.Column(db.Integer, primary_key= True)
    descripcion = db.Column(db.String(255), nullable=False)

    usuarios = db.relationship("Usuario", back_populates="tipo")