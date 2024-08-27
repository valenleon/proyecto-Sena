from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required
from app import db

bp = Blueprint('home',__name__)

@bp.route('/home')
@login_required
def home():
    return render_template('home/index.html')