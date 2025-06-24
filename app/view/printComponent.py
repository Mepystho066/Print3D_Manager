from app.view.valuePrint import  ValuePrint
from app.controller.saveValues import *
from app.view.color import Color
class PrintComponent():
    def __init__(self):
       self.viewport()
    def body(self):
        with dpg.group(horizontal=True):
                with dpg.group(horizontal=False): 
                    with dpg.group(tag="GrupoTextos",horizontal=False,width=200):
                            printName = dpg.add_input_text(label="Print name",
                                                           tag="printName",
                                                           parent="GrupoTextos")
                            dpg.add_button(label="Add img",callback=self.addFileView)
                            dpg.add_file_dialog(
                                 directory_selector=True,show=False,
                                 callback=self.fileCall,tag="file_dialog_id",
                                 cancel_callback=self.cancel_callback,width=700,
                                 height=400)
                    with dpg.group(horizontal=False):
                        self.Gestor()
                        self.Valores()
                        ValuePrint()
                with dpg.group(horizontal=False):
                             ## tabla de usuarios 
                            #self.table_prints()

                            Color()
                
    ## Guardar un usuario             
    #dpg.add_button(label="Enviar", width=50, height=50, callback=saveValues)
    def viewport(self):
        with dpg.child_window(height=300):
            self.body()

    def addFileView(self):
            dpg.configure_item("file_dialog_id",show=True)

    def viewBatches(self):
        if dpg.get_value("Tipo") == "Tanda":
            dpg.configure_item("cuantityTands",show=True)
        else:
            dpg.configure_item("cuantityTands",show=False,default_value=0)

    def fileCall(self,sender, app_data):
        print('OK was clicked.')
        print("Sender: ", sender)
        print("App Data: ", app_data)

    def cancel_callback(self,sender, app_data):
        print('Cancel was clicked.')
        print("Sender: ", sender)
        print("App Data: ", app_data)


    def Gestor(self):
        with dpg.group(horizontal=False):
            Tipo= dpg.add_radio_button(
                 label="Tipo",tag="Tipo",items=["Cantidad","Tanda"],
                 callback=self.viewBatches,horizontal=True
                 )
            cuantityTands = dpg.add_input_int(
                 label="Cuantity tands",tag="cuantityTands",
                 show=False,default_value=1,width=200
                 )
    
    def Valores(self):
        with dpg.group(tag="GrupoValores",horizontal=False,width=200):
            cantidad = dpg.add_input_int(
                 label="Cantidad",tag="Cantidad",parent="GrupoValores"
                 )
            flamentoUtilizado = dpg.add_input_double(
                label="Filament used",tag="filamentUsed",
                parent="GrupoValores",format='%.2f'
                )
            valorLaminador = dpg.add_input_double(
                 label="Valor Laminador",tag="ValorLaminador",
                 parent="GrupoValores",format='%.2f')


    def table_prints(self):
        with dpg.child_window(height=115,border=True):
            with dpg.table(tag="user_table", header_row=True) as selectablerows:
                dpg.add_table_column(label="Name")
                dpg.add_table_column(label="Filament")
                dpg.add_table_column(label="TimePirnt")
                dpg.add_table_column(label="Value")
                for i in range(15):
                    with dpg.table_row():
                        for j in range(4):
                            dpg.add_selectable(label=f"{i} {j}", callback=self.clb_selectable, user_data=j)

    def clb_selectable(self, sender, app_data, user_data):
        print(f"Row {user_data}")