import mysql.connector

try:
    cnx = mysql.connector.connect( host = '127.0.0.1',
                        user = 'root', 
                        password = 'root',
                        database = 'dbms')
    cursor = cnx.cursor()
except mysql.connector.Error as e:
        print(e)
        print("Connection not established.")


def get_country_id(country_name):
    cursor.execute("SELECT country_id FROM Countries WHERE country_name='%s'" % (country_name))
    return list(cursor.fetchone())[0]

def get_indicator_code(indicator_name):
    cursor.execute("SELECT indicator_code FROM Indicators WHERE indicator_name='%s'" % (indicator_name))
    return list(cursor.fetchone())[0]

def get_all_years():
    cursor.execute("SELECT DISTINCT year FROM Stats")
    return cursor.fetchall()

def get_countries_by_name():
    cursor.execute("SELECT country_name FROM Countries")
    return cursor.fetchall()
    
def get_indicators_by_name():
    cursor.execute("SELECT indicator_name FROM Indicators")
    return list(cursor.fetchall())

def get_all_years_by_country_indicator(country_name, indicator_name):
    country_id = get_country_id(country_name)
    indicator = get_indicator_code(indicator_name)
    indicator = indicator.replace('.', '_').lower()
    cursor.execute("SELECT Year, %s FROM Stats WHERE country_id='%s'" % (indicator, country_id))
    for i in list(cursor.fetchall()):
        print(i)

def get_values_by_country_indicator(country_name, indicator_name):
    country_id = get_country_id(country_name)
    indicator = get_indicator_code(indicator_name)
    indicator = indicator.replace('.', '_').lower()
    cursor.execute("SELECT %s FROM Stats WHERE country_id='%s'" % (indicator, country_id))
    for i in list(cursor.fetchall()):
        print(i)

#get_values_by_country_indicator('Angola', 'Total reserves (% of total external debt)')


