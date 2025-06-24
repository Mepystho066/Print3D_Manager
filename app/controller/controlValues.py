import dearpygui.dearpygui as dpg
def Cost():
#se agrega un valor agregado que seria el del trabajador 
    
    cantidad =dpg.get_value("Cantidad")
    valorLaminador=dpg.get_value("ValorLaminador")
    filamentoUtilizado=dpg.get_value("filamentUsed")
    printerCost = dpg.get_value("PrinterCost") or 1 
    ReturnYeas = dpg.get_value("ReturnYeas") or 1
    hoursCommercialUse =dpg.get_value("hoursCommercialUse")
    maintenanceCostTotal =dpg.get_value("maintenanceCostTotal")
    pago = 200
    trabajador= pago * filamentoUtilizado  
    impresoraAhorro = (pago *Time())+(printerCost/ReturnYeas)*Time()
    
    #print(ValueElectricity(),impresoraAhorro)
    if dpg.get_value("Tipo")=="Tanda":
        cantidadTanda= dpg.get_value("cuantityTands")
        TimeTotal= (Time()*cantidadTanda)
        
    else:
        TimeTotal= Time()    
    Total = cantidad *(valorLaminador+trabajador)
    valorNeto = Total -(cantidad*(trabajador+ValueElectricity()))
    dpg.set_value("Electricidad",ValueElectricity())
    dpg.set_value("PagoTrabajador",trabajador)
    dpg.set_value("ValorAhorroImpresora",impresoraAhorro)
    dpg.set_value("ValorTotal",Total)
    dpg.set_value("ValorNeto",valorNeto)
   
def Time():
    horas= dpg.get_value("Horas") or 0
    minutos = dpg.get_value("Minutos") or 1
    time_total_value = (minutos/60) + horas
    #print('Time', time_total_value)
    return time_total_value

def ValueElectricity():
    precioLuzKWh = dpg.get_value("EnergyCost") or 1
    consumoImpresora = dpg.get_value("energyConsumption") or 1
    valorTotal= (Time()*consumoImpresora)*precioLuzKWh
    #print('Value electricicty ',precioLuzKWh,consumoImpresora,valorTotal)
    return valorTotal

def Labot_cost():
    workingTime=dpg.get_value("workingTime") or 1
    costWorkinTime = dpg.get_value("costWorkinTime") or 1 
    postProcessingTime=dpg.get_value("postProcessingTime") or 1
    postProcessingCost=dpg.get_value("postProcessingCost") or 1

    trabajo_por_hora  =(workingTime * costWorkinTime) + (postProcessingTime * postProcessingCost)

    dpg.set_value("totalLaborCost",trabajo_por_hora)