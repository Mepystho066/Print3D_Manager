from app.service.db_service import request_query

class Addres :
    NAME_CLASS = 'Address'

    #  Definimos los atributos
    def __init__(self,id:str=None,user_id:str=None,county: str=None,city: str=None,addres: str=None,postalCode: str=None):
        self.id=id
        self.user_id=user_id
        self.county=county
        self.city=city
        self.addres=addres
        self.postalCode=postalCode

    # Aquí definimos como se muestra el objeto cuando se llama
    def __str__(self):
        return f"id={self.id},user_id={self.user_id},county={self.county},city={self.city},addres={self.addres},postalCode={self.postalCode}"

    # Definimos como se muestra una serie de objetos
    def __repr__(self):
        return f"id={self.id},user_id={self.user_id},county={self.county},city={self.city},addres={self.addres},postalCode={self.postalCode}"

    # -- Definimos metodos el objeto --

    def save(self):
        # Aqui van los atributos
        query = f'INSERT INTO {self.NAME_CLASS}(user_id,county,city,addres,postalCode) VALUES(?,?,?,?,?)'
        parameter = (self.user_id,self.county,self.city,self.addres,self.postalCode)
        print('save ', parameter)
        return request_query(query, parameter)

    @classmethod
    def create(clss,user_id,county,city,addres,postalCode):
        # Agregar los atributos que van a entrar
        obj = clss(user_id=user_id,county=county,city=city,addres=addres,postalCode=postalCode)
        print('create ' , obj)
        data = obj.save()
        return data

    def get_fom_db(self):
        query = f' SELECT * FROM {self.NAME_CLASS}'
        table = request_query(query).fetchall()
        return [self.for_obj(row) for row in table]

    @classmethod
    def for_obj(clss, param):
        obj = clss(user_id=param[1],county=param[2],city=param[3],addres=param[4],postalCode=param[5])
        obj.id = param[0] # Para objener el id si el objeto tine un id
        return obj
    @classmethod
    def get_for_id (clss,ID):
        query = f'SELECT * From {clss.NAME_CLASS} WHERE id = ?'
        row = request_query(query,(ID)).fetchall()
        obj =clss(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4],row[0][5])
        return obj

    @classmethod
    def get_for_name (clss,name):
        query = f'SELECT * From {clss.NAME_CLASS} WHERE name = ?'
        row = request_query(query,(name)).fetchall()
        obj =clss(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4],row[0][5])
        return obj


    def create_table(self):
        query = f'''CREATE TABLE IF NOT EXISTS {self.NAME_CLASS} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id integer DEFAULT None,
                    county TEXT DEFAULT None ,
                    city TEXT DEFAULT None ,
                    addres TEXT DEFAULT None  ,
                    postalCode integer DEFAULT None ,
                    UNIQUE(county,city,addres,postalCode),                 
                    FOREIGN KEY (user_id) REFERENCES User(id)
                    )'''
        request_query(query)

    def drop_table(self):
        query = f'DROP TABLE IF EXISTS {self.NAME_CLASS}'
        request_query(query)

