from registro_crypto import app
from flask import render_template


@app.route('/')
def index():
    
    datos = [{'id':1,'moneda_from':'EUR','cantidad_from':1000,'moneda_to':'BTC','cantidad_to':0.1},
             {'id':2,'moneda_from':'BTC','cantidad_from':0.05,'moneda_to':'ETH','cantidad_to':2},
             {'id':3,'moneda_from':'ETH','cantidad_from':1,'moneda_to':'ETH','cantidad_to':750}]
    
    
    return render_template('index.html',pageTitle='inicio', data=datos )