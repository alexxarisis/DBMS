from model.dataload import dataloadTemplate
from model import databaseConnector, dataFormatter, plotter
from controller import controller
from client import view

if __name__ == '__main__':
    dataloadTemplate.createAndLoadData()
    myController = controller.Controller(
        databaseConnector.DatabaseConnector(),
        dataFormatter.DataFormatter(),
        plotter.PlotMaker()
    )
    view.ClientView(myController)