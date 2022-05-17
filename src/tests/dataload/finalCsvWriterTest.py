from dataload.fileInformant import FileInformant
from dataload.finalCsvsWriter import CsvWriter

from os import listdir
from os.path import join
import pandas as pd

def runTests(fileInfo: FileInformant):
    CsvWriter(fileInfo).createCsvs()
    
    filesCreatedTest(fileInfo)
    countriesCsvTest(fileInfo)
    indicatorsCsvTest(fileInfo)
    statsCsvTest(fileInfo)

def filesCreatedTest(fileInfo):
    files = [f for f in listdir(fileInfo.outputDir)]
    assert 'countries.csv' in files, 'CsvWriter: countries.csv not found or created.'
    assert 'indicators.csv' in files, 'CsvWriter: indicators.csv not found or created.'
    assert 'stats.csv' in files, 'CsvWriter: stats.csv not found or created.'

def countriesCsvTest(fileInfo):
    countryCsv = pd.read_csv(join(fileInfo.outputDir, fileInfo.countriesCsv))
    expectedColumnHeaders = ['Country Code', 'Region', 'IncomeGroup', 'TableName', 'SpecialNotes']
    columnHeaders = [str(x) for x in countryCsv.columns]
    assert expectedColumnHeaders == columnHeaders, 'CsvWriter: countries.csv has wrong column headers/names.'
    assert not (len(countryCsv.index) <  25), 'CsvWriter: countries.csv | Data is missing'
    assert not (len(countryCsv.index) >  25), 'CsvWriter: countries.csv | Data is more than expected'

def indicatorsCsvTest(fileInfo):
    indicatorsCsv = pd.read_csv(join(fileInfo.outputDir, fileInfo.indicatorsCsv))
    expectedColumnHeaders = ['INDICATOR_CODE', 'INDICATOR_NAME', 'SOURCE_NOTE', 'SOURCE_ORGANIZATION']
    columnHeaders = [str(x) for x in indicatorsCsv.columns]
    assert expectedColumnHeaders == columnHeaders, 'CsvWriter: indicators.csv has wrong column headers/names.'
    assert not (len(indicatorsCsv.index) <  55), 'CsvWriter: indicators.csv | Data is missing'
    assert not (len(indicatorsCsv.index) >  55), 'CsvWriter: indicators.csv | Data is more than expected'
    
def statsCsvTest(fileInfo):
    # load indicators from the indicators'csv
    indicatorsCsv = pd.read_csv(join(fileInfo.outputDir, fileInfo.indicatorsCsv))
    indicators = [str(x) for x in indicatorsCsv['INDICATOR_CODE']]
    # load the stats csv
    statsCsv = pd.read_csv(join(fileInfo.outputDir, fileInfo.statsCsv))
    expectedColumnHeaders = ['Country ID', 'Year'] + indicators
    columnHeaders = [str(x) for x in statsCsv.columns]
    assert expectedColumnHeaders == columnHeaders, 'CsvWriter: stats.csv has wrong column headers/names.'
    assert not (len(statsCsv.index) <  1525), 'CsvWriter: stats.csv | Data is missing'
    assert not (len(statsCsv.index) >  1525), 'CsvWriter: stats.csv | Data is more than expected'