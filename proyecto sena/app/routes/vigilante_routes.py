from flask import Blueprint, render_template, redirect, request, url_for
from app.models.vigilante import Vigilante
from app import db

bp = Blueprint('vigilante', __name__)

@bp.route('/Vigilante')
def index():
    data = Vigilante.query.all()
    return render_template('vigilantes/index.html', data=data)

@bp.route('/Vigilante/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']

        new_vigilante = Vigilante(nombre=nombre, telefono=telefono)
        db.session.add(new_vigilante)
        db.session.commit()

        return redirect(url_for('vigilante.index'))
    
    return render_template('vigilantes/add.html')

@bp.route('/Vigilante/edit/<int:idVigilante>', methods=['GET', 'POST'])
def edit(idVigilante):
    vigilante = Vigilante.query.get_or_404(idVigilante)

    if request.method == 'POST':
        vigilante.nombre = request.form['nombre']
        vigilante.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('vigilante.index'))

    return render_template('vigilantes/edit.html', vigilante=vigilante)

@bp.route('/Vigilante/delete/<int:idVigilante>')
def delete(idVigilante):
    vigilante = Vigilante.query.get_or_404(idVigilante)
    
    db.session.delete(vigilante)
    db.session.commit()

    return redirect(url_for('vigilante.index'))
