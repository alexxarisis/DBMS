

class Controller:
    def __init__(self, dbConnector, dataFormatter, plotMaker):
        self.dbConnector = dbConnector
        self.dataFormatter = dataFormatter
        self.plotMaker = plotMaker

    def getIndicators(self):
        return self.dbConnector.getIndicators()

    def getCountries(self):
        return self.dbConnector.getCountries()

    def getYears(self):
        return self.dbConnector.getYears()

    def makeTimelinePlot(self, indicators, countries, fromYear, toYear, perYears):
        data =  self.dataFormatter.getTimelineData(indicators, countries,
                                                        fromYear, toYear)
        years = self.dbConnector.getYearsInRange(fromYear, toYear)
        self.plotMaker.makeTimelinePlot(data, years, indicators, perYears)
    
    def makeBarPlot(self, indicators, countries, fromYear, toYear, perYears):
        print('haha made a bar plot yuhoo')

    def makeScatterPlot(self, indicators, countries, fromYear, toYear, perYears):
        data = self.dataFormatter.getScatterData(indicators, countries,
                                                        fromYear, toYear)
        self.plotMaker.makeScatterPlot(data, indicators, countries, perYears)