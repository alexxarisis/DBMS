# Local application imports
from createFinalCsvs import Writer
from loadToMySQL import Loader

def createAndLoadData():
    Writer().createCsvs()
    Loader().loadToMySQL()

if __name__ == '__main__':
    createAndLoadData()