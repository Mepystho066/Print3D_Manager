import dearpygui.dearpygui as dpg
from app.controller.saveValues import saveSettings
from app.controller.getValues import settingsValues
from  app.controller.controlValues import Labot_cost
class Settings():
    def __init__(self):
        with dpg.group(horizontal=True):
            with dpg.group(horizontal=False):
                with dpg.child_window(height=200,width=420):
                    self.Values()
                    self.Electricity()
                with dpg.child_window(height=150,width=420):
                   self.MaintenanceAndMachineCost()
            with dpg.group(horizontal=False):
                with dpg.child_window(height=250):
                    self.laborCost()
                dpg.add_button(label='save', height=50, width=50,callback=saveSettings)
        settingsValues()
    
       
   #def visualEvent(self): 

    def Values(self):
         with dpg.group(tag="Values",width=200):
                        dpg.add_text("Values")
                        moneyValue = dpg.add_input_text(label="Money type",tag='MoneyType')
                        iva = dpg.add_input_double(label="IVA",tag='IVA',format='%.2f')

    def Electricity(self):
         with dpg.group(tag="Electricity",width=200):
            dpg.add_text("Electricity")
            energyConsumption=dpg.add_input_double(label="Energy consumption"+" Kw",tag="energyConsumption",format='%.2f')
            # Agregar descripciones
            with dpg.tooltip("energyConsumption"):
                dpg.add_text("Energia consumida por la impresora")
            energyCost = dpg.add_input_double(label="Energy cost kw/h ",tag='EnergyCost',format='%.2f')
            totalCost = dpg.add_input_double(label="Total Cost",tag='EnergyTotalCost',format='%.2f')
    
    def MaintenanceAndMachineCost(self):
        dpg.add_text("Maintenance and machine cost")
        with dpg.group(tag="MaintenanceAndMachineCost",width=200):
            printerCost= dpg.add_input_int(label="Printer Cost",tag='PrinterCost')
            returnOnInvestment = dpg.add_slider_int(label="Return on investment Yeas",max_value=10,tag='ReturnYeas')
            hoursCommercialUse= dpg.add_slider_int(label="hours of commercial use",tag="hoursCommercialUse",vertical=False,default_value=1,max_value=24,width=25)
            repairCosts = dpg.add_slider_int(label="Repair costs %",tag="repairCosts",vertical=False,default_value=1,max_value=100,width=25)
            #callback llamada para que se actualice
            maintenanceCostTotal = dpg.add_slider_int(label="Maintenance cost total",tag="maintenanceCostTotal",vertical=False,width=25)
    
    
    def laborCost(self):
        dpg.add_text("Labor cost")
        with dpg.group(height=90,horizontal=False):
            with dpg.group(height=90, horizontal=True):
                with dpg.child_window(height=90,width=500):
                    with dpg.group(tag="LaborCost"):
                        dpg.add_text("Preparación de la impresión")
                        workingTime = dpg.add_input_int(label="working time Hours",tag="workingTime",callback=Labot_cost)
                        # Agregar descripciones
                        with dpg.tooltip("workingTime"):
                            dpg.add_text("texto")
                        costWorkinTime =dpg.add_input_double(label="Cost working time",tag="costWorkinTime",format='%.2f',callback=Labot_cost)
            with dpg.child_window(height=90,width=650):
                with dpg.group(tag="PostProcessing"):
                    dpg.add_text("Post-processing")
                    postProcessingTime= dpg.add_slider_int(label="Post-processing time Hours",tag="postProcessingTime",callback=Labot_cost)
                    postProcessingCost = dpg.add_input_double(label="Post-processing time Cost",tag="postProcessingCost",format='%.2f',callback=Labot_cost)
            
            totalLaborCost = dpg.add_slider_double(label="Total labor cost",tag="totalLaborCost",enabled=False,width=200,format='%.2f')

    