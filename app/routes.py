from app import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/atividades')
def atividadespage():
    return render_template('atividades.html')

@app.route('/contos')
def contospage():
    return render_template('contos.html')

@app.route('/cadastro')
def cadastropage():
    return render_template('cadastro.html')

