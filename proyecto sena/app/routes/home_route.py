from flask import Blueprint, redirect, render_template, request, url_for
from app import db

bp = Blueprint('home',__name__)

@bp.route('/')
def home():
    return render_template('home/index.html')