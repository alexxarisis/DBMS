# Standard library imports
from os import listdir
from os.path import join

# Third party imports
import pandas as pd

class CsvWriter:
    def __init__(self, fileInformant):
        # list of countries, in the order read
        self.countries = []
        self.fileInfo = fileInformant

    def createCsvs(self):
        print('CsvWriter: ')
        print('\tCreating csv\'s...', end=" ")
        self.__createCountriesCsv()
        self.__createStatsCsv()
        self.__createIndicatorsCsv()
        print('Done')

    def __createCountriesCsv(self):
        finalDf = pd.DataFrame()
        for filename in listdir(self.fileInfo.countriesDir):
            df = pd.read_csv(join(self.fileInfo.countriesDir, filename))
            finalDf = pd.concat([finalDf, df])

        # Drop unnecessary columns 
        finalDf = finalDf.drop(['Unnamed: 5', 'Unnamed: 4'], axis=1)
        # Export
        self.__exportToCsv(finalDf, self.fileInfo.countriesCsv)
        # save countries code in order read
        self.countries = finalDf['Country Code'].to_list()

    def __createStatsCsv(self):
        finalDf = pd.DataFrame()

        for filename in listdir(self.fileInfo.statsDir):
            df = pd.read_csv(join(self.fileInfo.statsDir, filename), skiprows=4)
            # Get specific ID of country based on country code
            code = df['Country Code'].drop_duplicates().loc[0]
            id = self.countries.index(code) + 1

            # Invert dataframe and drop unnessecary columns
            df = df.T
            df = df.drop(['Country Name', 'Country Code', 'Indicator Name', 'Unnamed: 65'])
            # Name headers based on each 'Indicator Code'
            df = df.rename(columns=df.iloc[0]).drop(df.index[0])
            # Make Years from index to a column
            df = df.reset_index()
            df = df.rename(columns={'index': 'Year'})

            # Keep only codes starting with the given strings
            wantedColumns = ('Year', 'BM', 'EG', 'GC.TAX')
            columnFilter = [col for col in df if col.startswith(wantedColumns)]
            df = df[columnFilter]

            # insert ID column based on country code
            df.insert(0, 'Country ID', id)
            finalDf = pd.concat([finalDf, df])
        # Export
        self.__exportToCsv(finalDf, self.fileInfo.statsCsv)

    def __createIndicatorsCsv(self):
        finalDf = pd.DataFrame()

        for filename in listdir(self.fileInfo.indicatorsDir):
            df = pd.read_csv(join(self.fileInfo.indicatorsDir, filename))
            df = df.drop(['Unnamed: 4'], axis = 1)
            finalDf = pd.concat([finalDf, df])

        # Keep specified non-duplicated columns
        finalDf = finalDf.drop_duplicates()
        finalDf = finalDf[finalDf['INDICATOR_CODE'].str.startswith('BM') | 
                            finalDf['INDICATOR_CODE'].str.startswith('EG') |
                            finalDf['INDICATOR_CODE'].str.startswith('GC.TAX') ]
        # Export
        self.__exportToCsv(finalDf, self.fileInfo.indicatorsCsv)

    def __exportToCsv(self, df, outputFileName):
        df.to_csv(join(self.fileInfo.outputDir, outputFileName), na_rep='NULL', index = False)