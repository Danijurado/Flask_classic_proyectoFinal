from registro_crypto import app
from flask import render_template
from registro_crypto.models import select_all

@app.route('/')
def index():
    registros = select_all()
    
    return render_template('index.html',pageTitle='inicio', data=registros )

@app.route('/purchase')
def compra():
    return 'aqui para comprar'