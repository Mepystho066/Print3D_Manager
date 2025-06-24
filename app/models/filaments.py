from app.service.db_service import request_query

class Filament :
    NAME_CLASS = 'Filamens'
    #  Definimos los atributos
    def __init__(self, id: str = None, name: str = None,color: str = None,company: str = None,value: int = None):
        self.id = id
        self.name = name
        self.color= color
        self.company = company
        self.value = value
    # Aquí definimos como se muestra el objeto cuando se llama

    def __str__(self):
        #return f"id={self.id},name={self.name},color={self.color},company={self.company},value={self.value}"
        return f"name={self.name},color={self.color},value={self.value}"
    # Definimos como se muestra una serie de objetos
    def __repr__(self):
        #return f"id={self.id},name={self.name},color={self.color},company={self.company},value={self.value}"
        return f"name={self.name},color={self.color},value={self.value}"
    # -- Definimos metodos el objeto --
    def save(self):
        # Aqui van los atributos
        query = f'INSERT INTO {self.NAME_CLASS}(name,color,company,value) VALUES(?,?,?,?)'
        parameter = (self.name,self.color,self.company,self.value  )
        print('save ', parameter)
        return request_query(query, parameter)

    @classmethod
    def create(clss, name,color ,company ,value):
        # Agregar los atributos que van a entrar
        obj = clss(name = name ,color= color ,company = company ,value = value)
        print('create ' , obj)
        data = obj.save()
        return data

    def get_fom_db(self):
        query = f' SELECT * FROM {self.NAME_CLASS}'
        table = request_query(query).fetchall()
        return [self.for_obj(row) for row in table]

    @classmethod
    def for_obj(clss, param):
        obj = clss(name= param[1])
        obj.id = param[0] # Para objener el id si el objeto tine un id
        return obj
    @classmethod
    def get_for_id (clss,ID):
        query = f'SELECT * From {clss.NAME_CLASS} WHERE id = ?'
        row = request_query(query,(ID)).fetchall()
        obj =clss(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4])
        return obj

    @classmethod
    def get_for_name (clss,name):
        query = f'SELECT * From {clss.NAME_CLASS} WHERE name = ?'
        row = request_query(query,(name)).fetchall()
        obj =clss(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4])
        return obj


    def create_table(self):
        query = f'''CREATE TABLE IF NOT EXISTS {self.NAME_CLASS} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT DEFAULT None ,
                    color TEXT,
                    company TEXT,
                    value DOUBLE
                    
                    )'''
        request_query(query)

    def drop_table(self):
        query = f'DROP TABLE IF EXISTS {self.NAME_CLASS}'
        request_query(query)

