import dearpygui.dearpygui as dpg
class PlottingBarrs():
    def __init__(self):
       self.viewport()
    
    def body(self):
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

        with dpg.tab(label="Grafica de Barras"):
            dpg.add_button(label="Actualizacion", callback=self.visualEvent)
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


    def viewport(self):
        self.body()

    def visualEvent(self): 
       pass
