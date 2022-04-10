# Local application imports
from model.dataload.finalCsvsWriter import Writer
from model.dataload.databaseLoader import Loader

def createAndLoadData():
    Writer().createCsvs()
    Loader().loadToMySQL()

if __name__ == '__main__':
    createAndLoadData()