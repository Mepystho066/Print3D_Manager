import sqlite3 as sql
from pathlib import Path


#### Esto es antigui 

"""
moneyType
iva
gastoEnergeticoImpresora
costoImpresora
retornoDeInvercionImpresora
usoDeHorasComerciales
costoRepacion
costoTotalMantenimiento
preparacionImpresionTiempoHoras
preparacionImpresionCosto
postProcesamientoTiempoHoras
postProcesamientoValor
costoTotalDeTrabajo
"""

dbPath ="App/db/data/setingsApi.db"
def createSettingDB():
    if False == Path(dbPath).exists():
        conn = sql.connect(dbPath)
        conn.commit()
        conn.close()
    
def createTable():
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS Setings (
    moneyType varchar(15), 
    iva dobule,
    gastoEnergeticoImpresora doble,
    costoImpresora doble,
    retornoDeInvercionImpresora double,
    usoDeHorasComerciales int ,
    costoRepacion double ,
    costoTotalMantenimiento doble,
    preparacionImpresionTiempoHoras int,
    preparacionImpresionCosto double ,
    postProcesamientoTiempoHoras int,
    postProcesamientoValor doble,
    costoTotalDeTrabajo doble)"""
    )
    conn.commit()
    conn.close()


def insertInfo(moneyType,iva,gastoEnergeticoImpresora,costoImpresora,retornoDeInvercionImpresora,
                usoDeHorasComerciales,costoRepacion,costoTotalMantenimiento,preparacionImpresionTiempoHoras,
                preparacionImpresionCosto,postProcesamientoTiempoHoras,postProcesamientoValor,costoTotalDeTrabajo):
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    instruccion = f"INSERT INTO Setings VALUES ('{moneyType}',{iva},{gastoEnergeticoImpresora},{costoImpresora},{retornoDeInvercionImpresora},{usoDeHorasComerciales},{costoRepacion},{costoTotalMantenimiento},{preparacionImpresionTiempoHoras},{preparacionImpresionCosto},{postProcesamientoTiempoHoras},{postProcesamientoValor},{costoTotalDeTrabajo})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
def mostrarTabla():
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Setings"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
if __name__ == "__main__":
    #createSettingDB()
    #createTable()
    #moneyType,iva,gastoEnergeticoImpresora,costoImpresora,retornoDeInvercionImpresora,usoDeHorasComerciales,costoRepacion,costoTotalMantenimiento,preparacionImpresionTiempoHoras,preparacionImpresionCosto,postProcesamientoTiempoHoras,postProcesamientoValor,costoTotalDeTrabajo
    insertInfo("Cop",2.2,2.2,3.2,5.2,2,10.2,22.2,3,3.2,2,1.2,2.2)
    mostrarTabla()