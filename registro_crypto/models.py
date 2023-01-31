import sqlite3
from config import ORIGIN_DATA


def select_all():
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute('SELECT id,fecha,hora,moneda_from,cantidad_from,moneda_to,cantidad_to FROM Movimientos order by fecha;')
    
    filas = res.fetchall()
    columnas = res.description
    
    resultado = []
    
    
    for fila in filas:
        dato = {}
        posicion = 0
        
        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)
    
    return resultado

def insert():
    pass

  