# Local application imports
from dataload.finalCsvsWriter import CsvWriter
from dataload.databaseCreator import DBCreator
from dataload.databaseLoader import DBLoader
from dataload.fileInformant import FileInformant

class DataLoader():
    def __init__(self):
        self.fileInfo = FileInformant()

    def createAndLoadData(self):
        CsvWriter(self.fileInfo).createCsvs()
        DBCreator(self.fileInfo).createDB()
        DBLoader(self.fileInfo).loadToMySQL()
        print('Data loaded successfully...')