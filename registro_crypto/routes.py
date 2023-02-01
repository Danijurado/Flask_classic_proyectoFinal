from registro_crypto import app
from flask import render_template
from registro_crypto.models import select_all
from registro_crypto.services import get_exchange
from flask import Flask, request

@app.route('/')
def index():
    registros = select_all()
    
    return render_template('index.html',pageTitle='inicio', data=registros )

@app.route('/purchase')
def compra():
    #get_exchange('EUR','BTC')
    #resultado = get_exchange('EUR','BTC')
    
    return render_template('purchase.html',pageTitle='compra')

@app.route('/purchase',methods = ['POST'])
def compra_post():
   from_currency = request.form["moneda_from"]
   to_currency = request.form['moneda_to']
   q = float(request.form['cantidad_from'])
   unit=get_exchange(from_currency,to_currency)
   
   cantidad_to = unit * q
   
   return render_template('purchase.html', pageTitle='compra',moneda_from=from_currency,cantidad_from=q,unit=1/unit,cantidad_to=cantidad_to)

@app.route('/status')
def status():
    return render_template('status.html', pageTitle='status')
  
