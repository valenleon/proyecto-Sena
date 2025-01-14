from flask import Blueprint, render_template, redirect, request, url_for
from app.models.computador import Computador
from app.models.usuario import Usuario
from app.models.perisferico import Perisferico
from app import db

bp = Blueprint('computador', __name__)

@bp.route('/Computador')
def index():
    data = Computador.query.all()
    perisferico = Perisferico.query.all()
    return render_template('computadores/index.html', data=data, perisferico=perisferico)

@bp.route('/Computador/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        marca = request.form['marca']
        perisferico_id = request.form['perisferico_id']

        new_computador = Computador(marca=marca, perisferico_id=perisferico_id)
        db.session.add(new_computador)
        db.session.commit()

        return redirect(url_for('computador.index'))
    
    perisferico = Perisferico.query.all()
    return render_template('computadores/add.html', perisfericos=perisferico)

@bp.route('/Computador/edit/<int:idComputador>', methods=['GET', 'POST'])
def edit(idComputador):
    computador = Computador.query.get_or_404(idComputador)

    if request.method == 'POST':
        computador.marca = request.form['marca']
        computador.perisferico_id = request.form['perisferico_id']

        db.session.commit()
        return redirect(url_for('computador.index'))
    
    perisferico = Perisferico.query.all()
    return render_template('computadores/edit.html', computador=computador, perisfericos=perisferico)

@bp.route('/Computador/delete/<int:idComputador>')
def delete(idComputador):
    computador = Computador.query.get_or_404(idComputador)

    db.session.delete(computador)
    db.session.commit()

    return redirect(url_for('computador.index'))