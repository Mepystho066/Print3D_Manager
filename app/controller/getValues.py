import dearpygui.dearpygui as dpg
from app.models.settings import Setting

def settingsValues():
    values = Setting().get_fom_db()
    #print(values.m)
    MoneyType = dpg.set_value('MoneyType',values[0].MoneyType)
    IVA = dpg.set_value('IVA',values[0].IVA)
    energyConsumption = dpg.set_value('energyConsumption',values[0].energyConsumption)
    EnergyCost = dpg.set_value('EnergyCost',values[0].EnergyCost)
    PrinterCost = dpg.set_value('PrinterCost',values[0].PrinterCost)
    ReturnYeas = dpg.set_value('ReturnYeas',values[0].ReturnYeas)
    hoursCommercialUse = dpg.set_value('hoursCommercialUse',values[0].hoursCommercialUse)
    repairCosts = dpg.set_value('repairCosts',values[0].repairCosts)
    workingTime = dpg.set_value('workingTime',values[0].workingTime)
    costWorkinTime = dpg.set_value('costWorkinTime',values[0].costWorkinTime)
    postProcessingTime = dpg.set_value('postProcessingTime',values[0].postProcessingTime)
    postProcessingCost = dpg.set_value('postProcessingCost',values[0].postProcessingCost)
    