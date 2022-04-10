# Local application imports
from dataload.finalCsvsWriter import CsvWriter
from dataload.databaseLoader import DBLoader
from dataload.fileInformant import FileInformant

class DataLoader():
    def __init__(self):
        self.fileInfo = FileInformant()

    def createAndLoadData(self):
        CsvWriter(self.fileInfo).createCsvs()
        DBLoader(self.fileInfo).loadToMySQL()

if __name__ == '__main__':
    DataLoader()