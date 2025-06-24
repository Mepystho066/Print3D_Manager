import dearpygui.dearpygui as dpg 
import datetime
#from datos import *
#dividir 2 millones de pesos 200 horas mensuales 10 pesos la hora o se puede tomar como 7 mill para el trabajador 
"""
Cobrabrar 10 pesos por hora de diseño 
coste de tiempo de imprecion 5000 por hora 
costo luz filamento y maquina lo del valorLaminador y agregar el coste de maquina 
dos años y medio de vida ultil 20.283
la depreciación por hora 1.500.000 /  = 75 pesos por hora de uso. lo cambio a 1.000
lo minimo que se paga de tiempo es 1 hora 

coste de luz , filamento, 75 pesos por hora 
#diseño de producto de continudidad es unao pero el precio de un moñeco es uno 
#sacar una tabla de cuanto custa vivir 

crear una tabla diferente para el coste del diseño 
"""
"""
Variables que se deberia tener en la base de datos 
Fecha 
Nombre 
tipo De impresion
valorLaminador
Valor Trabajador
Tiempo
ValorTotal

"""
fecha_actual = datetime.datetime.now()
year_actual = fecha_actual.year
month_actual = fecha_actual.month
day_actual = fecha_actual.day

DiccionarioVentas ={
    "fecha":[],
    "nombre":[],
    "tipo_Impresion":[],
    "filamentoColor":[],
    "tipoDeCantidades":[], 
    "cantidad":[],
    "filamentoUtilizado":[],
    "valorLaminador":[],
    "Tiempo":[],
    "electricidadValor":[],
    "PagoTrabajador":[],
    "ahorroImpresora":[], 
    "valorTotal":[],
    "valorNeto":[]
}

#def BaseDatosADiccionario():
    #MostrarOrdenLista(DiccionarioVentas)
def documentos():
    dpg.show_item_registry()
    dpg.show_documentation()
    dpg.show_imgui_demo()

    #dpg.show_about()
    #dpg.show_style_editor()
    #dpg.show_debug()
    #dpg.show_metrics()
    #dpg.show_font_manager()
 
def Vista_tanda():
    if dpg.get_value("Tipo")=="Tanda":
        dpg.configure_item("CantidadTanda",show=True)
    else:
        dpg.configure_item("CantidadTanda",show=False,default_value=0)

def Ventas():
     
    with dpg.tab(label="Venta"):
        Fecha= dpg.add_date_picker(label="Fecha",tag="Fecha",default_value={'month_day': day_actual , 'year': 123, 'month': month_actual})
        dpg.add_group(tag="GrupoTextos",horizontal=False,width=300)
        Nombre= dpg.add_input_text(label="Nombre",tag="NombreCliente",parent="GrupoTextos")
        Impresion= dpg.add_input_text(label="Tipo De Impresion",tag="Impresion",parent="GrupoTextos")
        FilamentoColor= dpg.add_input_text(label="color",tag="ColorFilamento",parent="GrupoTextos")
        
        Tipo= dpg.add_radio_button(label="Tipo",tag="Tipo",items=["Cantidad","Tanda"],callback=Vista_tanda,horizontal=True) 
        dpg.add_input_int(label="Cantidad Tanda",tag="CantidadTanda",show=False,default_value=1)  
        dpg.add_group(tag="GrupoValores",horizontal=True,width=200)
        Cantidad = dpg.add_input_int(label="Cantidad",tag="Cantidad",parent="GrupoValores")
        FlamentoUtilizado=dpg.add_input_double(label="Filamento Utilizado",tag="FilamentoUtilizado",parent="GrupoValores",format='%.2f')
        ValorLaminador= dpg.add_input_double(label="Valor Laminador",tag="ValorLaminador",parent="GrupoValores",format='%.2f')
        
        dpg.add_group(tag="GupoTiempo",horizontal=True)
        Horas= dpg.add_slider_int(label="Horas",tag="Horas",parent="GupoTiempo",vertical=True,default_value=1,max_value=72,width=25,callback=Costos)
        Minutos= dpg.add_slider_int(label="Minutos",tag="Minutos",parent="GupoTiempo",vertical=True,default_value= 1,max_value=59,width=25,callback=Costos)
       
        Electricidad = dpg.add_slider_double(label="Electricidad",tag="Electricidad",enabled=False,width=200,format='%.2f')
        #mostrar total de la suma de si es cantidad con tanda y el valor de los trabajadores  
        dpg.add_group(tag="GurpoValores",horizontal=True)
        
        PagoTrabajador = dpg.add_slider_double(label="Pago Trabajador",tag="PagoTrabajador",enabled=False,width=200,format='%.2f')
        ahorroImpresora =dpg.add_slider_double(label="Valor ahorroImpresora",tag="ValorAhorroImpresora",enabled=False,width=200,format='%.2f')
        ValorTotal = dpg.add_slider_double(label="Valor Total",tag="ValorTotal",enabled=False,width=200,format='%.2f')
        ValorNeto = dpg.add_slider_double(label="Valor Neto",tag="ValorNeto",enabled=False,width=200,format='%.2f')
        dpg.add_button(label="Enviar",user_data=[Fecha,Nombre,Impresion,FilamentoColor,Tipo,
                                                 Cantidad,FlamentoUtilizado,ValorLaminador,
                                                 Tiempo(),Electricidad,PagoTrabajador,
                                                 ahorroImpresora,ValorTotal,ValorNeto],callback=Valores)
           
    #algo que muestre toda la informacion de las sumas y restas asi sacar el valor neto se va as asacar un 5% del valor ganado Del trabajador

def Costos():
#se agrega un valor agregado que seria el del trabajador 
    cantidad =dpg.get_value("Cantidad")
    valorLaminador=dpg.get_value("ValorLaminador")
    filamentoUtilizado=dpg.get_value("FilamentoUtilizado")
    trabajador= 200 * filamentoUtilizado  
    impresoraAhorro = (200 *Tiempo())+(2000000/20000)*Tiempo()
    if dpg.get_value("Tipo")=="Tanda":
        cantidadTanda= dpg.get_value("CantidadTanda")
        TiempoTotal= (Tiempo()*cantidadTanda)
        
    else:
        TiempoTotal= Tiempo()    
    Total = cantidad *(valorLaminador+trabajador)
    valorNeto = Total -(cantidad*(trabajador+ValorElectricidad()))
    dpg.set_value("Electricidad",ValorElectricidad())
    dpg.set_value("PagoTrabajador",trabajador)
    dpg.set_value("ValorAhorroImpresora",impresoraAhorro)
    dpg.set_value("ValorTotal",Total)
    dpg.set_value("ValorNeto",valorNeto)
   
def Tiempo():
    horas= dpg.get_value("Horas") or 0
    minutos = dpg.get_value("Minutos") or 0
    tiempoT = (minutos/60) + horas
    return tiempoT

def ValorElectricidad():
    precioLuzKWh = 800.74
    consumoImpresora = 0.3
    valorTotal= (Tiempo()*consumoImpresora)*precioLuzKWh
    return valorTotal

def GraficasCostos():
    with dpg.tab(label="Graficas Costos"):
        dpg.add_input_text(label="Nombre Trabajador")
        dpg.add_input_double(label="Pago")
       
def Valores(sender,app_data,user_data):
    fechas= dpg.get_value(user_data[0])
    fecha = "{}/{}/20{}".format(fechas['month_day'],fechas['month'],(fechas['year']-100))
    nombre = dpg.get_value(user_data[1])
    impresion= dpg.get_value(user_data[2])
    filamentoColor= dpg.get_value(user_data[3])
    tipoDeCantidades= dpg.get_value(user_data[4])
    cantidad= dpg.get_value(user_data[5])
    filamentoUtilizado= dpg.get_value(user_data[6])
    ValorLaminador= dpg.get_value(user_data[7])
    tiempo= user_data[8]
    valorElectricidad= dpg.get_value(user_data[9])
    pagoTrabajador= dpg.get_value(user_data[10])
    ahorroImpresora= dpg.get_value(user_data[11])
    valorTotal= dpg.get_value(user_data[12])
    valorNeto= dpg.get_value(user_data[13])

    DiccionarioVentas["fecha"].append(fecha)
    DiccionarioVentas["nombre"].append(nombre)
    DiccionarioVentas["tipo_Impresion"].append(impresion)
    DiccionarioVentas["filamentoColor"].append(filamentoColor)
    DiccionarioVentas["tipoDeCantidades"].append(tipoDeCantidades)
    DiccionarioVentas["cantidad"].append(cantidad)
    DiccionarioVentas["filamentoUtilizado"].append(filamentoUtilizado)
    DiccionarioVentas["valorLaminador"].append(ValorLaminador)
    DiccionarioVentas["Tiempo"].append(tiempo)
    DiccionarioVentas["electricidadValor"].append(valorElectricidad)
    DiccionarioVentas["PagoTrabajador"].append(pagoTrabajador)
    DiccionarioVentas["ahorroImpresora"].append(ahorroImpresora)
    DiccionarioVentas["valorTotal"].append(valorTotal)
    DiccionarioVentas["valorNeto"].append(valorNeto)
    insertRow(fecha,nombre,impresion,filamentoColor,tipoDeCantidades,cantidad,
                filamentoUtilizado,ValorLaminador,tiempo,valorElectricidad,
                pagoTrabajador,ahorroImpresora,valorTotal,valorNeto)
    """Fecha,Nombre,Impresion,FilamentoColor,Tipo,
        Cantidad,FlamentoUtilizado,ValorLaminador,
        Tiempo(),ValorElectricidad(),PagoTrabajador,
        ahorroImpresora,ValorTotal,valorNeto"""

def actualizacionGraficaTotal():
    espacio=[]
    for i in range(len(DiccionarioVentas["valorNeto"])):
        espacio.append(i)   

    dpg.set_value("series 0",[espacio,DiccionarioVentas["PagoTrabajador"]])
    dpg.set_value("series 1",[espacio,DiccionarioVentas["ahorroImpresora"]])
    dpg.set_value("series 2",[espacio,DiccionarioVentas["valorTotal"]])
    dpg.set_value("series 3",[espacio,DiccionarioVentas["valorNeto"]])

    espacio1 = [i*10 for i in range(len(DiccionarioVentas["valorNeto"]))]
    espacio2 = [i*10+1 for i in range(len(DiccionarioVentas["valorNeto"]))]
    espacio3 = [i*10+2 for i in range(len(DiccionarioVentas["valorNeto"]))]
    espacio4 = [i*10+3 for i in range(len(DiccionarioVentas["valorNeto"]))]
    dpg.set_value("series 0.0",[espacio1,DiccionarioVentas["PagoTrabajador"]])
    dpg.set_value("series 0.1",[espacio2,DiccionarioVentas["ahorroImpresora"]])
    dpg.set_value("series 0.2",[espacio3,DiccionarioVentas["valorTotal"]])
    dpg.set_value("series 0.3",[espacio4,DiccionarioVentas["valorNeto"]])

def GraficaTotal():
    espacio=[]
    for i in range(len(DiccionarioVentas["valorNeto"])):
        espacio.append(i)
    with dpg.tab(label="Gafica"):
        dpg.add_button(label="Actualizacion", callback=actualizacionGraficaTotal)
        with dpg.plot(tag="GraficaInferior",width=-1,height=-1):
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")
            
            dpg.add_line_series(espacio,DiccionarioVentas["PagoTrabajador"],label="Pago Trabajador",parent="y_axis",tag="series 0")
            dpg.add_button(label="boton",parent=dpg.last_item(),callback= lambda : dpg.delete_item("series 0"))#MenuPersonalizado
            dpg.add_line_series(espacio,DiccionarioVentas["ahorroImpresora"],label="Ahorro Impresora",parent="y_axis",tag="series 1")
            dpg.add_button(label="boton",parent=dpg.last_item(),callback= lambda : dpg.delete_item("series 1"))
            dpg.add_line_series(espacio,DiccionarioVentas["valorTotal"],label="Valor Total",parent="y_axis",tag="series 2")
            dpg.add_button(label="boton",parent=dpg.last_item(),callback= lambda : dpg.delete_item("series 2"))
            dpg.add_line_series(espacio,DiccionarioVentas["valorNeto"],label="Valor Neto",parent="y_axis",tag="series 3")
            dpg.add_button(label="boton",parent=dpg.last_item(),callback= lambda : dpg.delete_item("series 3"))

def GraficaPagos():
    with dpg.tab(label="Grafica de Barras"):
      dpg.add_button(label="Actualizacion", callback=actualizacionGraficaTotal)
      with dpg.plot(label="Bar Series", height=-1, width=-1,tag="GraficaInferior_2"):
        dpg.add_plot_legend()
        # create x axis
        dpg.add_plot_axis(dpg.mvXAxis, label="Ahorros", no_gridlines=True)
        dpg.set_axis_ticks(dpg.last_item(), (("PagoTrabajador", 0), ("ahorroImpresora", 11), ("valorTotal", 22),("valorNeto", 33)))
        # create y axis
        dpg.add_plot_axis(dpg.mvYAxis, label="Score", tag="yaxis_tag")
        # add series to y axis
        espacio1 = [i*10 for i in range(len(DiccionarioVentas["valorNeto"]))]
        espacio2 = [i*10+1 for i in range(len(DiccionarioVentas["valorNeto"]))]
        espacio3 = [i*10+2 for i in range(len(DiccionarioVentas["valorNeto"]))]
        espacio4 = [i*10+3 for i in range(len(DiccionarioVentas["valorNeto"]))]
        dpg.add_bar_series(espacio1, DiccionarioVentas["PagoTrabajador"], label="PagoTrabajador", weight=1, parent="yaxis_tag",tag="series 0.0")
        dpg.add_bar_series(espacio2, DiccionarioVentas["ahorroImpresora"], label="ahorroImpresora", weight=1, parent="yaxis_tag",tag="series 0.1")
        dpg.add_bar_series(espacio3, DiccionarioVentas["valorTotal"], label="valorTotal", weight=1, parent="yaxis_tag",tag="series 0.2")
        dpg.add_bar_series(espacio4, DiccionarioVentas["valorNeto"], label="valorNeto", weight=1, parent="yaxis_tag",tag="series 0.3")


def BarralateralSuperior():
    with dpg.tab_bar(label="BarraLateral"):    
        Ventas()
        GraficasCostos()

def BarraLateralInferior():
    with dpg.tab_bar():
        GraficaTotal()   
        GraficaPagos()

dpg.create_context()
dpg.create_viewport(title="DashBoard")
#Ventana Principal
with dpg.window(label="Principal",tag="Principal"):
   # BaseDatosADiccionario()
    dpg.add_button(label="Documentos",callback=documentos)
    BarralateralSuperior()
    BarraLateralInferior()

dpg.set_primary_window("Principal",True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()