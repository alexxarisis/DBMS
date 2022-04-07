# Local application imports
from databaseConnector import DatabaseConnector
from dataformat import DataFormatter
from plots import PlotMaker

class Engine:
    def __init__(self):
        self.dbConnector = DatabaseConnector()
        self.dataFormatter = DataFormatter()
        self.plotMaker = PlotMaker()

    def getIndicators(self):
        return self.dbConnector.getIndicators()

    def getCountries(self):
        return self.dbConnector.getCountries()

    def getYears(self):
        return self.dbConnector.getYears()

    def makeTimelinePlot(self, indicators, countries, fromYear, toYear, perYears):
        data =  self.dataFormatter.getFormattedData(indicators, countries,
                                                        fromYear, toYear)
        years = self.dbConnector.getYearsInRange(fromYear, toYear)

        self.plotMaker.makeTimelinePlot(data, years, indicators)
