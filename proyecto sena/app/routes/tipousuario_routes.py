from flask import Blueprint, render_template, redirect, request, url_for
from app.models.tipousuario import TipoUsuario
from flask_login import login_required
from app import db

bp = Blueprint('tipousuario', __name__)
tipo_usuario = TipoUsuario()

@bp.route('/Tipousuario')
@login_required
def index():
    data = TipoUsuario.query.all()
    return render_template('tipousuarios/index.html', data=data)

@bp.route('/Tipousuario/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        
        new_tipousuario = TipoUsuario(descripcion=descripcion)
        db.session.add(new_tipousuario)
        db.session.commit()
        
        return redirect(url_for('tipousuario.index'))

    return render_template('tipousuarios/add.html')

@bp.route('/Tipousuario/edit/<int:idTipoUsuario>', methods=['GET', 'POST'])
def edit(idTipoUsuario):
    tipousuario = TipoUsuario.query.get_or_404(idTipoUsuario)

    if request.method == 'POST':
        tipousuario.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('tipousuario.index'))

    return render_template('tipousuarios/edit.html', tipousuario=tipousuario)

@bp.route('/Tipousuario/delete/<int:idTipoUsuario>')
def delete(idTipoUsuario):
    tipousuario = TipoUsuario.query.get_or_404(idTipoUsuario)
    
    db.session.delete(tipousuario)
    db.session.commit()

    return redirect(url_for('tipousuario.index'))
