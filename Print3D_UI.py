import dearpygui.dearpygui as dpg 
import dearpygui.demo as demo
from app.service.creation_tables import createTables
from app.view.userComponent import UserComponent
from app.view.printComponent import PrintComponent
from app.view.adddata.graphs import ViewGraphs
from app.view.settings import Settings
from app.view.style import Sytle

class Main():
    def __init__(self):   
        ### Mostrar la aplicacion                      
        dpg.create_context()
        dpg.create_viewport(title="DashBoard")
        #Ventana Principal
        self.body()    
        #Sytle()    
        dpg.set_primary_window("Principal",True)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
    
    def body(self):
        with dpg.window(label="Principal",tag="Principal"):
            with dpg.tab_bar():
                with dpg.tab(label="Add data"):
                    dpg.add_button(label="Documentos",callback=self.domuments)
                    UserComponent()
                    PrintComponent()
                    ViewGraphs()
                with dpg.tab(label="Settings"):
                    Settings()
  
    def domuments(self):
        #demo.show_demo()
        dpg.show_style_editor()
        
if __name__ == "__main__":
    createTables()
    Main()
    