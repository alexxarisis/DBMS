import csv
from mysql.connector import connect, Error

# Must be with '/' and NOT '\' for the sql statement
csv_dir = 'C:/Users/alexx/Desktop/DBMS/csvs/final/'

countries_csv = 'countries.csv'
stats_csv = 'stats.csv'
indicators_csv = 'indicators.csv'

def connect_to_database(cursor):
    cursor.execute('DROP DATABASE dbms')
    print('Creating database...', end=' ')
    cursor.execute('CREATE DATABASE IF NOT EXISTS dbms')
    cursor.execute('USE dbms')
    print('Done')

def get_headers():
    with open(csv_dir + stats_csv, newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        formatted_headers =  [header.replace('.', '_').lower() for header in headers]
        return formatted_headers[4:]

def create_tables(cursor):
    print('Creating tables...', end=' ')

    create_country_table_query = '''
        CREATE TABLE IF NOT EXISTS Countries(
            country_id INT NOT NULL,
            country_code VARCHAR(3),
            region VARCHAR(64),
            income_group VARCHAR(64),
            country_name VARCHAR(64),
            special_notes TEXT,
            PRIMARY KEY (country_id)
        )
        '''

    create_stats_table_query = '''
        CREATE TABLE IF NOT EXISTS Stats(
            country_id INT NOT NULL,
            year YEAR NOT NULL,
            PRIMARY KEY (country_id, year),
            FOREIGN KEY (country_id) REFERENCES Countries(country_id)
        '''

    for header in get_headers():
        create_stats_table_query += ', \n' + header + ' DOUBLE'
    create_stats_table_query += ')'

    create_indicator_table_query = '''
        CREATE TABLE IF NOT EXISTS Indicators(
            indicator_id INT NOT NULL,
            indicator_code VARCHAR(32),
            indicator_name TEXT,
            source_note TEXT,
            source_organization TEXT,
            PRIMARY KEY (indicator_id)
        )
        '''
    
    cursor.execute(create_country_table_query)
    cursor.execute(create_stats_table_query)
    cursor.execute(create_indicator_table_query)
    
    print('Done')

def load_csv(cursor):
    print('Loading files...', end=' ')
    cursor.execute('SET GLOBAL local_infile=\'ON\';')

    load_countries_query = "LOAD DATA LOCAL INFILE '"  + csv_dir + countries_csv + """'
        INTO TABLE Countries
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\r\n'
        IGNORE 1 LINES
    """

    load_stats_query = "LOAD DATA LOCAL INFILE '"  + csv_dir + stats_csv + """'
        INTO TABLE Stats
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\r\n'
        IGNORE 1 LINES
    """

    load_indicators_query = "LOAD DATA LOCAL INFILE '"  + csv_dir + indicators_csv + """'
        INTO TABLE Indicators
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        LINES TERMINATED BY '\r\n'
        IGNORE 1 LINES
    """
    
    cursor.execute(load_countries_query)
    cursor.execute(load_stats_query)
    cursor.execute(load_indicators_query)

    print('Done')

def load_files_to_mysql():
    try:
        with connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            allow_local_infile=True
        ) as connection:
            with connection.cursor() as cursor:
                connect_to_database(cursor)
                create_tables(cursor)
                load_csv(cursor)
                connection.commit()
                print('Completed.')

                cursor.execute('SELECT indicator_id FROM Indicators')
                print(cursor.fetchall())
                connection.close()
    except Error as e:
        print(e)

load_files_to_mysql()