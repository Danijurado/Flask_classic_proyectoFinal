import sqlite3
from config import ORIGIN_DATA
from registro_crypto.conexion import Conexion

def select_all():
    connect = Conexion('SELECT id,fecha,hora,moneda_from,cantidad_from,moneda_to,cantidad_to FROM Movimientos order by fecha;')
    
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

def insert(registro):
    connectInsert = Conexion("insert into movimientos(moneda_from,cantidad_from,moneda_to,cantidad_to) values(?,?,?,?)",registro)
    connectInsert.con.commit()
    connectInsert.con.close()
    

    
