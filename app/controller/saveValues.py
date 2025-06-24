import dearpygui.dearpygui as dpg
from app.controller.componentsEvent import tagsDates,settingsDate
from app.models.addres import Addres
from app.models.user import User
from app.models.settings import Setting
from app.models.filaments import Filament
def saveValues():
    # User
    userVal = tagsDates()[0]
    addresVal = tagsDates()[1]
    User().create(userVal[1],userVal[2],userVal[3])

    # Addres
    if userVal[0] != '':
        Addres().create(userVal[0],addresVal[0],addresVal[1],addresVal[2],addresVal[3])
    else:
        userid = User().get_fom_db()
        Addres().create(userid[-1].id,addresVal[0],addresVal[1],addresVal[2],addresVal[3])

def saveSettings():
    Setting().drop_table()
    Setting().create_table()
    values_app = settingsDate()
    Setting().create(values_app[0],values_app[1],values_app[2],
                    values_app[3],values_app[4],values_app[5],
                    values_app[6],values_app[7],values_app[8],
                    values_app[9],values_app[10],values_app[11])

def saveColor():
    dateFilament = tagsDates()[3]
    Filament().create(dateFilament[0],dateFilament[1],dateFilament[2],dateFilament[3])
    test =  Filament().get_fom_db()
    for i in enumerate(test):
        print(i)
        for e in i :
            print(e)

    
