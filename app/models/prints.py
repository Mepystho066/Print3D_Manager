from app.service.db_service import request_query

class Print :
    NAME_CLASS = 'Print'

    #  Definimos los atributos
    def __init__(self, id: str = None,name: str = None,image:str = None,timePrint:str = None,value:int=None,filamentFK:str = None):

        self.id = id
        self.name = name
        self.image = image
        self.timePrint = timePrint
        self.value = value 
        self.filamentFK = filamentFK
    # Aquí definimos como se muestra el objeto cuando se llama
    def __str__(self):
        return f"id={self.id},name={self.name},image={self.image},timePrint={self.timePrint},value={self.value},filamentFK={self.filamentFK}"

    # Definimos como se muestra una serie de objetos
    def __repr__(self):
        return f"id={self.id},name={self.name},image={self.image},timePrint={self.timePrint},value={self.value},filamentFK={self.filamentFK}"

    # -- Definimos metodos el objeto --

    def save(self):
        # Aqui van los atributos
        query = f'INSERT INTO {self.NAME_CLASS}(name,image,timePrint,value,filamentFK) VALUES(?,?,?,?,?)'
        parameter = (self.name,self.image,self.timePrint,self.value,self.filamentFK)
        print('save ', parameter)
        return request_query(query, parameter)

    @classmethod
    def create(clss, name,image,timePrint,value,filamentFK):
        # Agregar los atributos que van a entrar
        obj = clss(name,image,timePrint,value,filamentFK)
        print('create ' , obj)
        data = obj.save()
        return data

    def get_fom_db(self):
        query = f' SELECT * FROM {self.NAME_CLASS}'
        table = request_query(query).fetchall()
        return [self.for_obj(row) for row in table]

    @classmethod
    def for_obj(clss, param):
        obj = clss(name= param[1], image=param[2],timePrint=param[3],value=param[4],filamentFK=param[5])
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
        obj =clss(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4],row[0][5])
        return obj


    def create_table(self):
        query = f'''CREATE TABLE IF NOT EXISTS {self.NAME_CLASS} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT ,
                    name TEXT DEFAULT None,
                    image TEXT DEFAULT None,
                    timePrint INTEGER,
                    value INTEGER,
                    filamentFK INTEGER,
                    )'''
        request_query(query)

    def drop_table(self):
        query = f'DROP TABLE IF EXISTS {self.NAME_CLASS}'
        request_query(query)


class PrintCost:
    pass