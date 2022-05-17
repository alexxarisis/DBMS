from os import getcwd
from os.path import join
from pathlib import Path

from dataload.fileInformant import FileInformant

def runTests():
    fileInfo = FileInformant()
    dbmsDirectory = Path(getcwd()).parent
    countriesDirectory = join(dbmsDirectory, 'data\original\countries')
    statsDirectory = join(dbmsDirectory, 'data\original\stats')
    indicatorsDirectory = join(dbmsDirectory, 'data\original\indicators')
    outputDirectory = join(dbmsDirectory, 'data\\final')
    
    countriesDirectoryTest(countriesDirectory, fileInfo)
    statsDirectoryTest(statsDirectory, fileInfo)
    indicatorsDirectoryTest(indicatorsDirectory, fileInfo)
    outputFilesDirectoryTest(outputDirectory, fileInfo)
    return fileInfo

def countriesDirectoryTest(countriesDirectory, fileInfo):
    assert countriesDirectory == fileInfo.countriesDir, "FileInformant: Countries data directory not found or is wrong"

def statsDirectoryTest(statsDirectory, fileInfo):
    assert statsDirectory == fileInfo.statsDir, "FileInformant: Stats data directory not found or is wrong"

def indicatorsDirectoryTest(indicatorsDirectory, fileInfo):
    assert indicatorsDirectory == fileInfo.indicatorsDir, "FileInformant: Indicators data directory not found or is wrong"

def outputFilesDirectoryTest(outputDirectory, fileInfo):
    assert outputDirectory == fileInfo.outputDir, "FileInformant: Output data directory not found or is wrong"