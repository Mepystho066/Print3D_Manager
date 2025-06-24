import sqlite3 as sql




#### Antiguo 

class Tables:
    def __init__(self, path):
        self.connection = sql.connect(path) 
        self.cursor = self.connection.cursor()

    def createTables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS facturas ( 
                id INTEGER PRIMARY KEY,
                printName TEXT,
                cuantityPrints integer,
                totalCost integer
        )''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                lastName TEXT NOT NULL,
                email TEXT 
                conunty TEXT,
                city TEXT , 
                addres TEXT, 
                postalCode  INTEGER,
                facturaFK Integer,
                FOREIGN key (facturaFK) References factura(Id)
            )
        ''')

        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS filamentCosts (
                id INTEGER PRYMARY KEY,
                cost INTEGER, 
                dateBuy date
            )''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS filaments  (
                id INTEGER PRIMARY KEY,
                filamentName TEXT,
                color COLOR ,
                companyName TEXT,
                filamentCostFK INTEGER,
                FOREIGN KEY (filamentCostFK) REFERENCES filamentCosts(id)
        )''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS printCosts (
                id INTEGER PRYMARY KEY,
                iva DOUBLE, 
                totalValue INTEGER,
                date date
        )''')

        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS prints (
                id INTEGER PRYMARY KEY, 
                name TEXT not null,
                img IMAGE,
                printTime INTEGER not null,
                filamentFK INTEGER,
                printCostFK INTEGER,
                FOREIGN KEY (filamentFK) REFERENCES filaments(id),
                FOREIGN KEY (printCostFK) REFERENCES  printCosts(id)
            )''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS userPrints(
                userIdFK integer,
                printIdFK integer,
                cuantityPrints integer,
                dateSell date,
                FOREIGN KEY (printIdFK) REFERENCES prints(id),
                FOREIGN KEY (userIdFK) REFERENCES users(id),
                PRIMARY KEY (userIdFK, printIdFK)
            )''')

        self.connection.commit()
    # Tables insetions 
    def insert_factura(self,printName,cuantityPrints,totalCost):
        self.connection.execute(''' INSERT INTO facturas (printName ,cuantityPrints ,totalCost) VALUES (?,?,?)''',
         (printName,cuantityPrints,totalCost))
        self.connection.commit()

    def insert_user(self, name, email):
        self.cursor.execute('''
            INSERT INTO users (name,lastName,email,conunty,city,addres,postalCode,facturaFK) VALUES (?,?,?,?,?,?,?,?)''',
             (name,lastName,email,conunty,city,addres,postalCode,facturaFK))
        self.connection.commit()

    def insert_filamentCosts():
        self.connection.execute(''' INSERT INTO filamentCosts (cost,dateBuy) VALUES (?,?)''', 
        (cost,dateBuy))
        self.connection.commit()

    def insert_filaments():
        self.connection.execute(''' INSERT INTO filaments (filamentName,color,companyName,filamentCostFK) VALUES (?,?,?,?)''', 
        (filamentName,color,companyName,filamentCostFK))
        self.connection.commit()

    def insert_printCosts():
        self.connection.execute(''' INSERT INTO printCosts (iva,totalValue,date) VALUES (?,?,?,?)''', (
            iva,totalValue,date))
        self.connection.commit()

    def insert_prints():
        self.connection.execute(''' INSERT INTO prints (name,img,printTime,filamentFK,printCostFK) VALUES (?,?,?,?,?)''', 
        (name,img,printTime,filamentFK,printCostFK))
        self.connection.commit()

    def insert_userPrints():
        self.connection.execute('''
        INSERT INTO userPrints (userIdFK,printIdFK,cuantityPrints,dateSell) VALUES (?,?,?,?)''', 
        (userIdFK,printIdFK,cuantityPrints,dateSell))
        self.connection.commit()

    def querysTable(self,nameTable):
        try :
            tables = ['facturas','users','filamentCosts','filaments','printCosts','prints','userPrints']
            if nameTable in tables:
                self.cursor.execute(f'SELECT * FROM {nameTable}')
                return self.cursor.fetchall()
        except ValueError: 
            print("filtro error ")
            return ValueError
            
    def querysTableCombine (self):
        pass
if __name__ =="__main__":
    tablas = Tables("App/db/data/dataBase.db")
    tablas.createTables()
    #tablas.insert_user()
    #tablas.insert_factura('mascara larga',3,60000)
    #users =tablas.queryTable('facturas')
    
    