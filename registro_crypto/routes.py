from registro_crypto import app
from flask import render_template
from registro_crypto.models import select_all
from registro_crypto.services import get_exchange
@app.route('/')
def index():
    registros = select_all()
    
    return render_template('index.html',pageTitle='inicio', data=registros )

@app.route('/purchase')
def compra():
    #get_exchange('EUR','BTC')
    #resultado = get_exchange('EUR','BTC')
    
    return render_template('purchase.html',pageTitle='compra')