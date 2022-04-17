

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
        # data
        data =  self.dataFormatter.getTimelineData(indicators, countries,
                                                        fromYear, toYear, perYears)
        # years
        years = self.dbConnector.getYearsInRange(fromYear, toYear)
        years = self.dataFormatter.getYearsByPeriod(years, perYears)
        # plot
        self.plotMaker.makeTimelinePlot(data, years, indicators)
    
    def makeBarPlot(self, indicators, countries, fromYear, toYear, perYears):
        print('haha made a bar plot yuhoo')

    def makeScatterPlot(self, indicators, countries, fromYear, toYear, perYears):
        # data
        data = self.dataFormatter.getScatterData(indicators, countries,
                                                        fromYear, toYear, perYears)
        # plot
        self.plotMaker.makeScatterPlot(data, indicators, countries)