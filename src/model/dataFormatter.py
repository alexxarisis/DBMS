# Local application imports
from model.databaseConnector import DatabaseConnector

class TimelineData():
    def __init__(self, country, indicator, values):
        self.name = country + ' - ' + indicator
        self.values = values

class ScatterData():
    def __init__(self, data):
        self.indicator1 = data[0]
        self.indicator2 = data[1]

class DataFormatter():
    def __init__(self):
        self.dbConnector = DatabaseConnector()

    # Returns a list of TimelineData objects
    def getTimelineData(self, indicators, countries, fromYear, toYear):
        data = []
        for indicator in indicators:
            for country in countries:
                values = self.dbConnector.selectBasedOnMultipleVariables(
                            indicator, country, fromYear, toYear)
                data.append(TimelineData(country, indicator, values))
        return data

    # Returns a ScatterData object
    def getScatterData(self, indicators, countries, fromYear, toYear):
        data = []
        for indicator in indicators:
            if (fromYear == toYear):
                data.append(self.dbConnector.
                    selectBasedOnYear(indicator, fromYear))
            else:
                data.append(self.dbConnector.selectBasedOnMultipleVariables(
                    indicator, countries[0], fromYear, toYear))
        return ScatterData(data)