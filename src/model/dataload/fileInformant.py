from os import getcwd
from os.path import join
from pathlib import Path

class FileInformant:
    def __init__(self):
        self.__getCsvFileNames()
        self.__getInputOutputDirectories()
        
    def __getCsvFileNames(self):
        self.countriesCsv = 'countries.csv'
        self.statsCsv = 'stats.csv'
        self.indicatorsCsv = 'indicators.csv'

    def __getInputOutputDirectories(self):
        # Get to csv's directory
        currentPath = Path(getcwd())
        csvsDir = join(currentPath.parent.absolute(), 'csvs')
        # Input csvs directories
        self.countriesDir = join(csvsDir, 'countries')
        self.statsDir = join(csvsDir, 'stats')
        self.indicatorsDir = join(csvsDir, 'indicators')
        # Output directory
        self.outputDir = join(csvsDir, 'final')


if __name__ == '__main__':
    fileInfo = FileInformant()
    print(fileInfo.countriesCsv)
    print(fileInfo.statsCsv)
    print(fileInfo.indicatorsCsv)
    print(fileInfo.countriesDir)
    print(fileInfo.statsDir)
    print(fileInfo.indicatorsDir)
    print(fileInfo.outputDir)