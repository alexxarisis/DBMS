# Standard library imports
from os import listdir
from os.path import join

# Third party imports
import pandas as pd

# Local application imports
from model.dataload.fileInformant import FileInformant

class Writer:
    def __init__(self):
        # {Country Code: ID} dictionary
        self.countryIDs = None
        self.fileInfo = FileInformant()

    def createCsvs(self):
        print('Creating csv\'s...', end=" ")
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
        # Make ID column
        finalDf = finalDf.reset_index(drop=True)
        finalDf.insert(0, 'Country ID', finalDf.index)
        self.__exportToCsv(finalDf, self.fileInfo.countriesCsv)
        # Also...
        # Fill dict with {country-id} values
        self.countryIDs = dict(zip(finalDf['Country Code'], finalDf['Country ID']))

    def __createStatsCsv(self):
        finalDf = pd.DataFrame()

        for filename in listdir(self.fileInfo.statsDir):
            df = pd.read_csv(join(self.fileInfo.statsDir, filename), skiprows=4)
            # Get specific ID of country
            code = df['Country Code'].drop_duplicates().loc[0]
            id = self.countryIDs.get(code)

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

            # insert ID column
            df.insert(0, 'Country ID', id)
            finalDf = pd.concat([finalDf, df])
        self.__exportToCsv(finalDf, self.fileInfo.statsCsv)

    def __createIndicatorsCsv(self):
        finalDf = pd.DataFrame()

        for filename in listdir(self.fileInfo.indicatorsDir):
            df = pd.read_csv(join(self.fileInfo.indicatorsDir, filename))
            df = df.drop(['Unnamed: 4'], axis = 1)
            finalDf = pd.concat([finalDf, df])

        finalDf = finalDf.drop_duplicates()
        finalDf = finalDf[finalDf['INDICATOR_CODE'].str.startswith('BM') | 
                            finalDf['INDICATOR_CODE'].str.startswith('EG') |
                            finalDf['INDICATOR_CODE'].str.startswith('GC.TAX') ]
        # Make IDs column
        finalDf.insert(0, column='Indicator ID', value=list(range(0, len(finalDf))))

        self.__exportToCsv(finalDf, self.fileInfo.indicatorsCsv)

    def __exportToCsv(self, df, outputFileName):
        df.to_csv(join(self.fileInfo.outputDir, outputFileName), na_rep='NULL', index = False)

if __name__ == '__main__':
    Writer().createCsvs()