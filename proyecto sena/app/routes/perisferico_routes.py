from flask import Blueprint, redirect, render_template, request, url_for
from app.models.perisferico import Perisferico
from app.models.computador import Computador
from app import db

bp = Blueprint('perisferico', __name__)

@bp.route('/Perisferico')
def index():
    data = Perisferico.query.all()
    datac = Computador.query.all()
    return render_template('perisfericos/index.html', data=data, datac=datac)

@bp.route('/Perisferico/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descripcion = request.form['descripcion']

        new_perisferico = Perisferico(descripcion=descripcion)
        db.session.add(new_perisferico)
        db.session.commit()

        return redirect(url_for('perisferico.index'))
    
    return render_template('perisfericos/add.html')

@bp.route('/Perisferico/edit/<int:idPerisferico>', methods=['GET', 'POST'])
def edit(idPerisferico):
    perisferico = Perisferico.query.get_or_404(idPerisferico)

    if request.method == 'POST':
        perisferico.descripcion = request.form['descripcion']

        db.session.commit()
        return redirect(url_for('perisferico.index'))
    
    return render_template('perisfericos/edit.html', perisferico=perisferico)

@bp.route('/Perisferico/delete/<int:idPerisferico>')
def delete(idPerisferico):
    perisferico = Perisferico.query.get_or_404(idPerisferico)

    db.session.delete(perisferico)
    db.session.commit()

    return redirect(url_for('perisferico.index'))