import dearpygui.dearpygui as dpg
from app.controller.saveValues import saveColor
from app.models.filaments import Filament
class Color():
    def __init__(self):
        with dpg.group(horizontal=True):
            with dpg.group(horizontal=True,width=250):
                self.table_color()
            with dpg.tree_node(label="Add Color"):
                with dpg.group(height=80, width=120,horizontal=True):
                    dpg.add_color_picker(height=100, width=100)
                    self.add_color()

    def add_color(self):
        with dpg.group(horizontal=False,height=100, width=120):
            dpg.add_input_text(label="Name", tag="filamentName")
            dpg.add_input_text(label="Color", tag= "filamentColor")
            dpg.add_input_text(label="Company",tag="company")
            dpg.add_input_text(label="Value", tag="filamentValue")
            with dpg.group(horizontal=False,height=20, width=20):
                dpg.add_button(label="Add",height=10,width=5,callback=saveColor)

    def table_color (self):
        with dpg.child_window(height=115):
            with dpg.table(tag="color_table", header_row=True) as selectablerows:
                dpg.add_table_column(label="Name")
                dpg.add_table_column(label="Color")
                dpg.add_table_column(label="Company")
                dpg.add_table_column(label="Value")

                for i in Filament().get_fom_db():
                    with dpg.table_row():
                        for j in range(3):
                            dpg.add_selectable(label=f"{j}", callback=self.clb_selectable, user_data=j)
               
    def clb_selectable(self, sender, app_data, user_data):
        print(f"Row {user_data}")