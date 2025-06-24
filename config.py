import os 
#Obtener la direccion acutal de la carpeta 
DB_PATH = os.path.dirname(os.path.abspath(__file__))
#Crear la carpteta
DB = os.path.join(DB_PATH+"/docs",'DB_TEST.db')

if __name__ == "__main__":
    print(DB)