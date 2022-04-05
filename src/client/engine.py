# Local application imports
from databaseConnector import DatabaseConnector

class Engine:
    def __init__(self):
        self.dbConnector = DatabaseConnector()

    def getIndicators(self):
        return self.dbConnector.getIndicators()

    def getCountries(self):
        return self.dbConnector.getCountries()

    def getYears(self):
        return self.dbConnector.getYears()