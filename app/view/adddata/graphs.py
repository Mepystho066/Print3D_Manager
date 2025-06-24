import dearpygui.dearpygui as dpg
from app.view.adddata.plottingBarrs import PlottingBarrs
from app.view.adddata.plottingGraph import PlottingGraphs
def ViewGraphs():
        with dpg.tab_bar():
                PlottingGraphs()
                PlottingBarrs()
