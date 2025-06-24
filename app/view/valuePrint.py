import dearpygui.dearpygui as dpg
from  app.controller.componentsEvent import *
from  app.controller.controlValues import Cost
class ValuePrint():
    def __init__(self):
       self.viewport()
    def body(self):
        with dpg.group(horizontal=True):
            with dpg.group(tag="GupoTiempo",horizontal=True):
                Horas = dpg.add_slider_int(label="Horas",tag="hours",vertical=True,default_value=1,max_value=72,width=25,callback=Cost)
                Minutos = dpg.add_slider_int(label="Minutos",tag="minuts",vertical=True,default_value= 1,max_value=59,width=25,callback=Cost)        
            #mostrar total de la suma de si es cantidad con tanda y el valor de los trabajadores  
            with dpg.group(tag="GurpoValores",horizontal=False):
                Electricidad = dpg.add_slider_double(label="Electricidad",tag="Electricidad",enabled=False,width=200,format='%.2f')
                PagoTrabajador = dpg.add_slider_double(label="Pago Trabajador",tag="PagoTrabajador",enabled=False,width=200,format='%.2f')
                ahorroImpresora =dpg.add_slider_double(label="Valor ahorroImpresora",tag="ValorAhorroImpresora",enabled=False,width=200,format='%.2f')
                ValorTotal = dpg.add_slider_double(label="Valor Total",tag="ValorTotal",enabled=False,width=200,format='%.2f')
                ValorNeto = dpg.add_slider_double(label="Valor Neto",tag="ValorNeto",enabled=False,width=200,format='%.2f')
        
    def visualEvent(self): 
       pass
    
    def viewport(self):
        with dpg.child_window(width=500,height=130):
            self.body()


    
    

    
