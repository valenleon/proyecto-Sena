from flask import Blueprint, render_template, redirect, request, url_for
from app.models.registro import Registro
from app.models.usuario import Usuario
from app.models.vigilante import Vigilante
from app import db

bp = Blueprint('registro', __name__)

@bp.route('/Registro')
def index():
    data = Registro.query.all()
    Usuarios = Usuario.query.all()
    vigilantes = Vigilante.query.all()

    return render_template('registros/index.html', data=data, Usuarios=Usuarios, vigilantes=vigilantes)

@bp.route('/Registro/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        usuarios_id = request.form['usuarios_id']
        vigilantes_id = request.form['vigilantes_id']
        fecha = request.form['fecha']
        hora = request.form['hora']
        
        new_registro = Registro(usuarios_id=usuarios_id, vigilantes_id=vigilantes_id, fecha=fecha, hora=hora)
        db.session.add(new_registro)
        db.session.commit()
        
        return redirect(url_for('registro.index'))
    
    usuarios = Usuario.query.all()
    vigilantes = Vigilante.query.all()

    return render_template('registros/add.html', usuario=usuarios, vigilant=vigilantes)

@bp.route('/Registro/edit/<int:idRegistro>', methods=['GET', 'POST'])
def edit(idRegistro):
    registro = Registro.query.get_or_404(idRegistro)

    if request.method == 'POST':
        registro.usuarios_id = request.form['usuarios_id']
        registro.vigilantes_id = request.form['vigilantes_id']
        registro.fecha = request.form['fecha']
        registro.hora = request.form['hora']

        db.session.commit()
        return redirect(url_for('registro.index'))
    
    usuarios_id = Usuario.query.all()
    vigilantes_id = Vigilante.query.all()

    return render_template('registros/edit.html', registro=registro, usuario=usuarios_id, vigilan=vigilantes_id )

@bp.route('/Registro/delete/<int:idRegistro>')
def delete(idRegistro):
    registro = Registro.query.get_or_404(idRegistro)

    db.session.delete(registro)
    db.session.commit()

    return redirect(url_for('registro.index'))