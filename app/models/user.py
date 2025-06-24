from app.service.db_service import request_query

class User :
    NAME_CLASS = 'Users'
    #  Definimos los atributos
    def __init__(self, id: str = None, name: str = None, lastname: str = None,email: str = None):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
    # Aquí definimos como se muestra el objeto cuando se llama
    def __str__(self):
        return f"id={self.id},name={self.name},lasname={self.lastname},email={self.email}"
    # Definimos como se muestra una serie de objetos
    def __repr__(self):
        return f"id={self.id},name={self.name},lastame={self.lastname},email={self.email}"
    # -- Definimos metodos el objeto --
    def save(self):
        # Aqui van los atributos
        query = f'INSERT INTO {self.NAME_CLASS}(name,lastname,email) VALUES(?,?,?)'
        parameter = (self.name, self.lastname,self.email)
        print('save ', parameter)
        return request_query(query, parameter)

    @classmethod
    def create(clss, name, lastname, email):
        # Agregar los atributos que van a entrar
        obj = clss(name=name,lastname=lastname,email=email)
        print('create ' , obj)
        data = obj.save()
        return data

    def get_fom_db(self):
        query = f' SELECT * FROM {self.NAME_CLASS}'
        table = request_query(query).fetchall()
        return [self.for_obj(row) for row in table]

    @classmethod
    def for_obj(clss, param):
        obj = clss(name= param[1], lastname= param[2],email= param[3])
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
        obj = clss(row[0][0], row[0][1], row[0][2], row[0][3])
        return obj

    @classmethod
    def get_User_Addres(clss, ID):
        #try:
            query = f'''SELECT * From {clss.NAME_CLASS} 
                        join Address adds ON Users.id = adds.user_id  
                        WHERE Users.id = ?'''
            row = request_query(query,(ID)).fetchall()
            # obj = clss(row[0][0], row[0][1], row[0][2], row[0][3])
            return row
        #except:
        #    print('Error User not in DB')



    def create_table(self):
        query = f'''CREATE TABLE IF NOT EXISTS {self.NAME_CLASS} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT DEFAULT None ,
                    lastname TEXT DEFAULT None,
                    email TEXT DEFAULT None,
                    UNIQUE(name,lastname,email)
                    )'''
        request_query(query)

    def drop_table(self):
        query = f'DROP TABLE IF EXISTS {self.NAME_CLASS}'
        request_query(query)

