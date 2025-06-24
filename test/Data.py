import sqlite3 as sql



#### Antiguo 

"""
Cobrabrar 10 pesos por hora de diseño 
coste de tiempo de imprecion 5000 por hora 
costo luz filamento y maquina lo del valorLaminador y agregar el coste de maquina 
dos años y medio de vida ultil 20.283
la depreciación por hora 1.500.000 /  = 75 pesos por hora de uso. lo cambio a 1.000
lo minimo que se paga de tiempo es 1 hora 

coste de luz , filamento, 75 pesos por hora 
#diseño de producto de continudidad es unao pero el precio de un moñeco es uno 
#sacar una tabla de cuanto custa vivir 

crear una tabla diferente para el coste del diseño 
"""
"""
Variables que se deberia tener en la base de datos 
Fecha 
Nombre 
tipo De impresion
valorLaminador
Valor Trabajador
Tiempo
ValorTotal

"""
fecha_actual = datetime.datetime.now()
year_actual = fecha_actual.year
month_actual = fecha_actual.month
day_actual = fecha_actual.day

DiccionarioVentas ={
    "fecha":[],
    "nombre":[],
    "tipo_Impresion":[],
    "filamentoColor":[],
    "tipoDeCantidades":[], 
    "cantidad":[],
    "filamentoUtilizado":[],
    "valorLaminador":[],
    "Tiempo":[],
    "electricidadValor":[],
    "PagoTrabajador":[],
    "ahorroImpresora":[], 
    "valorTotal":[],
    "valorNeto":[]
}



def createSettingDB():
    if False == Path(dbPath).exists():
        conn = sql.connect(dbPath)
        conn.commit()
        conn.close()
    
def createTableFilaments():
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE Filament (
    Id int private key identity (1,1) not null AUTO_INCREMENT,
    filamentName varchar(15),
    color color,
    furniture varchar(15),
    cuantity int ,
    filamentCostIdFK,
    Foreign key (filamentCostIdFK) References FilamentCost(Id) 
    )""")
    conn.commit()
    conn.close()

def createTableFilamentCosts():
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE FilamentCosts (
    Id int private key identity (1,1) not null AUTO_INCREMENT,
    cost int,
    dateBuy date,
    cauntity int 
    )""")
    conn.commit()
    conn.close()

def createTablePrints():
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE Prints (
    Id int private key identity (1,1) not null AUTO_INCREMENT,
    name varchar(50),
    img image,
    tunePrint int,
    filamentIdFK int,
    printCostIdFK int,
    Foreign key(filamentIdFK) References Filament(Id),
    Foreign key(printCostIdFK) References PrintCost(Id) 
    )""")
    conn.commit()
    conn.close()
    

def createTablePrintCosts():
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE PrintCosts (
    Id int private key identity (1,1) not null AUTO_INCREMENT,
    total double,
    iva int,
    )""")
    conn.commit()
    conn.close()


def createTableUsersPrints():
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE UsersPrints (
    cantidad int,
    dataSell date,
    userPrint
    printIdFK int,
    userIdFK int,
    Foreign key(PrintIdFK) References Prints(Id),
    Foreign key(userIdFK) References Users(Id),
    Primary KEY(PrintIdFK,UserIdFK)
    )""")
    conn.commit()
    conn.close()

def createTableUsers():
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE Setings (
    Id int private key identity (1,1) not null AUTO_INCREMENT,
    name varchar(10),
    lastName varchar(10),
    Country varchar(10),
    addres varchar,
    postalCode varchar,
    facturaIdFK int,
    Foreing key(facturaIdFK) References Factura (Id)
    )""")
    conn.commit()
    conn.close()

def createTableFactura():
    conn = sql.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE Setings (
    Id int private key identity (1,1) not null AUTO_INCREMENT,
    namePrint varchar,
    cuantityPrints int,
    totalCost int
    )""")
    conn.commit()
    conn.close()

def insertInfo(moneyType,iva,gastoEnergeticoImpresora,costoImpresora,retornoDeInvercionImpresora,usoDeHorasComerciales,costoRepacion,costoTotalMantenimiento,preparacionImpresionTiempoHoras,preparacionImpresionCosto,postProcesamientoTiempoHoras,postProcesamientoValor,costoTotalDeTrabajo):
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