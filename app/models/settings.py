from app.service.db_service import request_query

class Setting :
    NAME_CLASS = 'Settings'

    #  Definimos los atributos
    def __init__(self, MoneyType:str = None,
                 IVA:int = None,energyConsumption:int = None,EnergyCost:int = None,
                 PrinterCost:int = None,ReturnYeas:int = None,
                 hoursCommercialUse:int = None,repairCosts:int = None,
                 workingTime:int = None,costWorkinTime:int = None,
                 postProcessingTime:int= None,postProcessingCost:int = None):

        self.MoneyType = MoneyType
        self.IVA = IVA
        self.energyConsumption = energyConsumption
        self.EnergyCost =EnergyCost
        self.PrinterCost = PrinterCost
        self.ReturnYeas = ReturnYeas
        self.hoursCommercialUse = hoursCommercialUse
        self.repairCosts = repairCosts
        self.workingTime = workingTime
        self.costWorkinTime = costWorkinTime
        self.postProcessingTime = postProcessingTime
        self.postProcessingCost = postProcessingCost

    # Aquí definimos como se muestra el objeto cuando se llama
    def __str__(self):
        return f"""MoneyType={self.MoneyType},IVA={self.IVA},energyConsumption={self.energyConsumption},EnergyCost={self.EnergyCost},PrinterCost={self.PrinterCost},ReturnYeas={self.ReturnYeas},hoursCommercialUse={self.hoursCommercialUse},repairCosts={self.repairCosts},workingTime={self.workingTime},costWorkinTime={self.costWorkinTime},postProcessingTime={self.postProcessingTime} postProcessingCost ={self.postProcessingCost}"""

    # Definimos como se muestra una serie de objetos
    def __repr__(self):
        return f"""MoneyType={self.MoneyType},IVA={self.IVA},energyConsumption={self.energyConsumption},EnergyCost={self.EnergyCost},PrinterCost={self.PrinterCost},ReturnYeas={self.ReturnYeas},hoursCommercialUse={self.hoursCommercialUse},repairCosts={self.repairCosts},workingTime={self.workingTime},costWorkinTime={self.costWorkinTime},postProcessingTime={self.postProcessingTime} postProcessingCost ={self.postProcessingCost}"""

    # -- Definimos metodos el objeto --

    def save(self):
        # Aqui van los atributos
        query = f'''INSERT INTO {self.NAME_CLASS} 
                (MoneyType,IVA,energyConsumption,EnergyCost,
                PrinterCost,ReturnYeas,hoursCommercialUse,repairCosts,
                workingTime,costWorkinTime,postProcessingTime,
                postProcessingCost) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''
                
            
        parameter = (self.MoneyType,self.IVA,self.energyConsumption,
                    self.EnergyCost,self.PrinterCost,self.ReturnYeas,
                    self.hoursCommercialUse,self.repairCosts,self.workingTime,
                    self.costWorkinTime,self.postProcessingTime,self.postProcessingCost)
       # print('save ', parameter)
        return request_query(query, parameter)

    @classmethod
    def create(clss, MoneyType,IVA,energyConsumption,EnergyCost,PrinterCost,ReturnYeas,hoursCommercialUse,repairCosts,workingTime,costWorkinTime,postProcessingTime,postProcessingCost):
        # Agregar los atributos que van a entrar
        obj = clss(MoneyType,IVA,energyConsumption,EnergyCost,PrinterCost,ReturnYeas,hoursCommercialUse,repairCosts,workingTime,costWorkinTime,postProcessingTime,postProcessingCost)
        print('create ' , obj)
        data = obj.save()
        return data

    def get_fom_db(self):
        query = f' SELECT * FROM {self.NAME_CLASS}'
        table = request_query(query).fetchall()
        return [self.for_obj(row) for row in table]

    @classmethod
    def for_obj(clss, param):
        obj = clss(param[0],param[1],param[2],param[3],
        param[4],param[5],param[6],param[7],param[8],param[9],param[10],param[11])
        #obj.id = param[0] # Para objener el id si el objeto tine un id
        return obj
    @classmethod
    def get_for_id (clss,ID):
        query = f'SELECT * From {clss.NAME_CLASS} WHERE id = ?'
        row = request_query(query,(ID)).fetchall()
        obj =clss(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4],
                row[0][5],row[0][6],row[0][7],row[0][8],row[0][9],
                row[0][10],row[0][11])
        return obj

    @classmethod
    def get_for_name (clss,name):
        query = f'SELECT * From {clss.NAME_CLASS} WHERE name = ?'
        row = request_query(query,(name)).fetchall()
        obj = clss(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4],
                row[0][5],row[0][6],row[0][7],row[0][8],row[0][9],
                row[0][10],row[0][11])
        return obj

    def create_table(self):
        query = f'''CREATE TABLE IF NOT EXISTS {self.NAME_CLASS} (  
                    MoneyType VARCHAR(10),
                    IVA DOUBLE ,
                    energyConsumption DOUBLE ,
                    EnergyCost DOUBLE,
                    PrinterCost DOUBLE ,
                    ReturnYeas DOUBLE ,
                    hoursCommercialUse DOUBLE ,
                    repairCosts DOUBLE ,
                    workingTime DOUBLE ,
                    costWorkinTime DOUBLE,
                    postProcessingTime DOUBLE,
                    postProcessingCost DOUBLE
                    )'''
        request_query(query)
        
    def drop_table(self):
        query = f'DROP TABLE IF EXISTS {self.NAME_CLASS}'
        request_query(query)

