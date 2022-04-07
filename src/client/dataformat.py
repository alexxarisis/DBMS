# Local application imports
from databaseConnector import DatabaseConnector

class DataHolder():
    def __init__(self, country, indicator, values):
        self.name = country + ' - ' + indicator
        self.values = values

class DataFormatter():
    def __init__(self):
        self.dbConnector = DatabaseConnector()

    def getFormattedData(self, indicators, countries, fromYear, toYear):
        data = []
        for indicator in indicators:
            for country in countries:
                data.append(DataHolder(country, indicator,
                    self.dbConnector.getTimelineValues(indicator, country, fromYear, toYear)))
        return data