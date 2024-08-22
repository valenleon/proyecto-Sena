from flask import Blueprint, render_template, redirect, request, url_for
from app.models.usuario import Usuario
from app.models.tipousuario import TipoUsuario
from app.models.computador import Computador

from app import db

bp = Blueprint('usuario', __name__)

@bp.route('/Usuario')
def index():
    data = Usuario.query.all()
    return render_template('usuarios/index.html', data=data)

@bp.route('/Usuario/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        tipousuario_id = request.form['tipousuario_id']
        computador_id = request.form['computador_id']
        
        new_usuario = Usuario(nombre=nombre, tipousuario_id=tipousuario_id, computador_id=computador_id)
        db.session.add(new_usuario)
        db.session.commit()
        
        return redirect(url_for('usuario.index'))
    tipossss = TipoUsuario.query.all()
    computador = Computador.query.all()
    return render_template('usuarios/add.html', tipos=tipossss, computadores=computador)

@bp.route('/Usuario/edit/<int:idUsuario>', methods=['GET', 'POST'])
def edit(idUsuario): 
    usuario = Usuario.query.get_or_404(idUsuario)

    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.tipousuario_id = request.form['tipousuario_id']
        usuario.computador_id = request.form['computador_id']

        db.session.commit()
        return redirect(url_for('usuario.index'))
    
    tipossss = TipoUsuario.query.all()
    computador = Computador.query.all()

    return render_template('usuarios/edit.html', usuario=usuario, tipos=tipossss, computadores=computador)

@bp.route('/Usuario/delete/<int:idUsuario>')
def delete(idUsuario):
    usuario = Usuario.query.get_or_404(idUsuario)

    db.session.delete(usuario)
    db.session.commit()

    return redirect(url_for('usuario.index'))