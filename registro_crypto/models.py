import sqlite3
from config import ORIGIN_DATA
from registro_crypto.conexion import Conexion
from  datetime import date,datetime

def select_all():
    connect = Conexion('SELECT id,fecha,moneda_from,cantidad_from,moneda_to,cantidad_to FROM Movimientos order by fecha;')
    
    filas = connect.res.fetchall()
    columnas = connect.res.description
    
    resultado = []
    
    
    for fila in filas:
        dato = {}
        posicion = 0
        
        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)
    connect.con.close()
    
    return resultado

def insert(moneda_from,cantidad_from,moneda_to,cantidad_to):
    now = datetime.today().isoformat()
    registro = [now, moneda_from,cantidad_from, moneda_to, cantidad_to ]
    connectInsert = Conexion("insert into Movimientos(fecha,moneda_from,cantidad_from,moneda_to,cantidad_to) values(?,?,?,?,?)",registro)
    connectInsert.con.commit()
    connectInsert.con.close()
    
    
def invertido():
    connect = Conexion('SELECT sum( cantidad_from) FROM Movimientos WHERE moneda_from="EUR"')
    return connect.res.fetchone()[0]

def recuperado():
    connect = Conexion('SELECT sum( cantidad_to) FROM Movimientos WHERE moneda_to="EUR"')
    return connect.res.fetchone()[0]
    
    
    

    
