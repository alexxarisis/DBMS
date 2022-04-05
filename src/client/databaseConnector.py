import mysql.connector

class DatabaseConnector:
    def __init__(self):
        self.__connect()

    def __del__(self):
        self.cnx.commit()
        self.cnx.close()
        
    def __connect(self):
        try:
            self.cnx = mysql.connector.connect( host = '127.0.0.1',
                                user = 'root', 
                                password = 'root',
                                database = 'dbms')
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as e:
                print(e)
                print("Connection not established.")

    def getIndicators(self):
        self.__executeQuery("SELECT indicator_name FROM Indicators")
        return [ind[0] for ind in self.cursor.fetchall()]

    def getCountries(self):
        self.__executeQuery("SELECT country_name FROM Countries")
        return [ind[0] for ind in self.cursor.fetchall()]

    def getYears(self):
        self.__executeQuery("SELECT DISTINCT year FROM Stats")
        return [ind[0] for ind in self.cursor.fetchall()]

    ########################
    ### STILL IN PROGRESS ###
    def getCountryID(self, country_name):
        self.__executeQuery("SELECT country_id FROM Countries WHERE country_name='%s'" % (country_name))
        return self.cursor.fetchone()[0]

    def getIndicatorCode(self, indicator_name):
        self.__executeQuery("SELECT indicator_code FROM Indicators WHERE indicator_name='%s'" % (indicator_name))
        return self.cursor.fetchone()[0]

    def get_all_years_by_country_indicator_STILLINPROGRESS(self, country_name, indicator_name):
        country_id = self.getCountryID(country_name)
        indicator = self.getIndicatorCode(indicator_name)
        indicator = indicator.replace('.', '_').lower()
        self.__executeQuery("SELECT Year, %s FROM Stats WHERE country_id='%s'" % (indicator, country_id))

    def get_values_by_country_indicator_STILLINPROGRESS(self, country_name, indicator_name):
        country_id = self.getCountryID(country_name)
        indicator = self.getIndicatorCode(indicator_name)
        indicator = indicator.replace('.', '_').lower()
        self.__executeQuery("SELECT %s FROM Stats WHERE country_id='%s'" % (indicator, country_id))


    ###############################
    def __executeQuery(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as e:
            print(e)