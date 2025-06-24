import dearpygui.dearpygui as dpg
from app.controller.componentsEvent import *
from app.models.user import User
from app.models.filaments import Filament

def search_user():
    userData = tagsDates()[0]
    def setInfo(ObjetUser):
        # User

        if False : #ObjetUser != list  :

            userID = dpg.set_value("userID", 'Error')
        else:
            userID = dpg.set_value("userID", ObjetUser[0][0])
            userName = dpg.set_value("userName", ObjetUser[0][1])
            lastName = dpg.set_value("lastName", ObjetUser[0][2])
            email = dpg.set_value("email", ObjetUser[0][3])
            # Addres
            county = dpg.set_value("county",ObjetUser[0][6])
            city = dpg.set_value("city",ObjetUser[0][7])
            addres = dpg.set_value("addres",ObjetUser[0][8])
            postalCode = dpg.set_value("postalCode",ObjetUser[0][9])

    if userData[0] != '' :
        #date_search = User().get_for_id(userData[0])
        date_search = User().get_fom_db()

        #setInfo(date_search)

    #elif userData[1] != ''  :
    #    date_search = User().get_for_name(userData[1])
    #    setInfo(date_search)

   

