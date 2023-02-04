from registro_crypto import app
from flask import render_template, redirect, url_for
from registro_crypto.models import select_all,insert, invertido, recuperado, cantidad_crypto, monedas_compradas
from registro_crypto.services import get_exchange
from flask import Flask, request
from datetime import date,datetime

@app.route('/')
def index():
    registros = select_all()
    
    for registro in registros:
       fecha = datetime.fromisoformat(registro['fecha'])
       registro['fecha'] = fecha.strftime('%Y-%m-%d')
       registro['hora'] = fecha.strftime('%H:%M')
    
    
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
   cantidad_to = request.form['cantidad_to']
   
   if not cantidad_to:
    unit=get_exchange(from_currency,to_currency)
    
    cantidad_to = unit * q
    
    return render_template('purchase.html', pageTitle='compra',moneda_from=from_currency,cantidad_from=q,unit=1/unit,cantidad_to=cantidad_to, moneda_to = to_currency)
   
   insert(moneda_from= from_currency,moneda_to= to_currency, cantidad_from= q, cantidad_to= cantidad_to)
   
   return redirect(url_for('index'))
   


@app.route('/status')
def status():
    inversion = invertido()
    inversion_recuperada = recuperado()
    valor_actual = 0
    mis_monedas = monedas_compradas()
    
    for moneda in mis_monedas:
        cantidad = cantidad_crypto(moneda)
        if cantidad > 0:
            valor_actual += get_exchange(moneda,'EUR')
            
    return render_template('status.html', pageTitle='status', invertido = inversion, recuperado = inversion_recuperada, valor_actual = valor_actual)
  
