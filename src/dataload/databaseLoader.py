# Standard library imports
from os.path import join

# Third party imports
import mysql.connector

class DBLoader:
    def __init__(self, fileInformant):
        self.fileInfo = fileInformant

    def loadToMySQL(self):
        print('DBLoader: ')
        self.__connect()
        self.__loadCsvs()

        self.cnx.commit()
        self.cnx.close()

    def __connect(self):
        print('\tConnecting... ', end=' ')
        try:
            self.cnx = mysql.connector.connect( host = '127.0.0.1',
                                user = 'root', 
                                password = 'root',
                                database='dbms',
                                allow_local_infile=True)
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as e:
                print(e)
                print("Connection not established.")
        print('Done')

    def __dataAreAlreadyLoaded(self, tableName):
        # returns 1 if there are any rows, otherwise 0
        self.__executeQuery('SELECT EXISTS (SELECT 1 FROM %s);' % (tableName))
        # convert 1,0 to True,False
        return bool(self.cursor.fetchone()[0])

    def __loadCsvs(self):
        print('\tLoading files...', end=' ')
        self.__executeQuery('SET GLOBAL local_infile=\'ON\';')

        self.__loadCsv(self.fileInfo.countriesCsv, 'Countries')
        self.__loadCsv(self.fileInfo.statsCsv, 'Stats')
        self.__loadCsv(self.fileInfo.indicatorsCsv, 'Indicators')
        print('Done')

    def __loadCsv(self, csvFile, tableName):
        if (self.__dataAreAlreadyLoaded(tableName)):
            return
        
        self.__executeQuery(self.__createLoadQuery(csvFile, tableName))

    def __createLoadQuery(self, csvFile, tableName):
        return  """
                LOAD DATA LOCAL INFILE '%s'
                INTO TABLE %s 
                FIELDS TERMINATED BY ','
                OPTIONALLY ENCLOSED BY '"'
                LINES TERMINATED BY '\r\n'
                IGNORE 1 LINES
            """ % (join(self.fileInfo.outputDir, csvFile).replace('\\', '/'), tableName)

    def __executeQuery(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as e:
            print(e)