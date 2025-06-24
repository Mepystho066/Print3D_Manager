from app.service.db_service import request_query

class Factura :
    NAME_CLASS = 'Facturas'
    #  Definimos los atributos
    def __init__(self, id: str = None, user_fk: str = None,date_sell: str = None, values: str = None):
        self.id = id
        self.user_fk = user_fk
        self.date_sell = date_sell
        self.values = values
    # Aquí definimos como se muestra el objeto cuando se llama
    def __str__(self):
        return f"id={self.id},user_fk={self.user_fk},date_sell={self.date_sell},values={self.values}"
    # Definimos como se muestra una serie de objetos
    def __repr__(self):
        return f"id={self.id},user_fk={self.user_fk},date_sell={self.date_sell},values={self.values}"
    # -- Definimos metodos el objeto --
    def save(self):
        # Aqui van los atributos
        query = f'INSERT INTO {self.NAME_CLASS}(user_fk,date_sell,values) VALUES(?,?,?)'
        parameter = (self.name, self.user_fk)
        print('save ', parameter)
        return request_query(query, parameter)

    @classmethod
    def create(clss, name,user_fk):
        # Agregar los atributos que van a entrar
        obj = clss(user_fk=user_fk)
        print('create ' , obj)
        data = obj.save()
        return data

    def get_fom_db(self):
        query = f' SELECT * FROM {self.NAME_CLASS}'
        table = request_query(query).fetchall()
        return [self.for_obj(row) for row in table]

    @classmethod
    def for_obj(clss, param):
        obj = clss(name= param[1], user_fk= param[2])
        obj.id = param[0] # Para objener el id si el objeto tine un id
        return obj
    @classmethod
    def get_for_id (clss,ID):
        query = f'SELECT * From {clss.NAME_CLASS} WHERE id = ?'
        row = request_query(query,(ID)).fetchall()
        obj =clss(row[0][0],row[0][1],row[0][2],row[0][3])
        return obj

    @classmethod
    def get_for_name (clss,name):
        query = f'SELECT * From {clss.NAME_CLASS} WHERE name = ?'
        row = request_query(query,(name)).fetchall()
        obj = clss(row[0][0], row[0][1])
        return obj


    def create_table(self):
        query = f'''CREATE TABLE IF NOT EXISTS {self.NAME_CLASS} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_fk INTEGER,
                    UNIQUE()
                    FOREIGN KEY (user_fk) REFERENCES Users(id)
                    )'''
        request_query(query)

    def drop_table(self):
        query = f'DROP TABLE IF EXISTS {self.NAME_CLASS}'
        request_query(query)

