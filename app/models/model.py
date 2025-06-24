from app.service.db_service import request_query

class Model:
    NAME_CLASS = 'Model'
    #  Definimos los atributos
    def __init__(self,test:str=None,test2:str=None):

        self.test = test
        self.test2 = test2

    #Aquí definimos como se muestra el objeto cuando se llama
    def __str__(self):
        return f"test={self.test},test2={self.test2}"

    #Definimos como se muestra una serie de objetos
    def __repr__(self):
        return f"test={self.test},test2={self.test2}"

    # -- Definimos metodos el objeto --

    def save(self):
        #Aqui van los atributos
        query = f'INSERT INTO {self.NAME_CLASS}s VALUES(?,?)'
        parameter = (self.test,self.test2)
        return request_query(query,parameter)
    
    @classmethod
    def create(clss,entrada1,entrada2):
        # Agregar los atributos que van a entrar 
        obj =  clss(entrada1,entrada2)
        data = obj.save()
        return data  

    def get_fom_db(self):
        query = f' SELECT * FROM {self.NAME_CLASS}s'
        table = request_query(query).fetchall()
        return [self.for_obj(row) for row in table]

    @classmethod
    def for_obj(clss,param):
        obj = clss(param[0],param[1])
        #new_objet.id = table[0] # Para objener el id si el objeto tine un id
        return obj
    
    def get_for_id(self):
        query = f'SELECT id From {self.NAME_CLASS}s'
        row = request_query(query)
        return self.for_obj(row)

    def create_table(self):
        query = f'''CREATE TABLE IF NOT EXISTS {self.NAME_CLASS}s (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                lastname TEXT
                )'''
        request_query(query)
    
    def drop_table(self):
        query = f'DROP TABLE IF EXISTS {self.NAME_CLASS}s '
        request_query(query)
    
    def test(self):
        print(self.Name)

if __name__=="__main__":
    # DEV TEST 
    test3 = Model()
    #test3.create_table()

    print(test3.get_fom_db())

