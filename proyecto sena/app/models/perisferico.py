from app import db

class Perisferico(db.Model):
    __tablename__ = 'perisferico'
    idPerisferico = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)

    computadores = db.relationship("Computador", back_populates="perisfericos")
