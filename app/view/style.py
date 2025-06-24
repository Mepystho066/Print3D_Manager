import dearpygui.dearpygui as dpg
class Sytle():
    def __init__(self):
       self.viewport()
    
    def body(self):

        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (69, 118, 162 ), category=dpg.mvThemeCat_Core)                                      
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,0)
            dpg.add_theme_style(dpg.mvStyleVar_ChildBorderSize,0)
            dpg.add_theme_style(dpg.mvStyleVar_ChildRounding,6)
        with dpg.theme_component(dpg.mvInputInt):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (148, 188, 224), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    def viewport(self):
        with dpg.theme() as global_theme:
            self.body()
        dpg.bind_theme(global_theme)
        #dpg.show_style_editor()

    def visualEvent(self): 
       pass
