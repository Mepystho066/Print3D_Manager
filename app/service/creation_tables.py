from app.models.addres import Addres
from app.models.user import User
from app.models.settings import Setting
from app.models.filaments import Filament
def createTables ():
    User().create_table()
    Addres().create_table()
    Filament().create_table()
    Setting().create_table()
