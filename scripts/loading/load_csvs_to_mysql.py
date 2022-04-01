import csv
import mysql.connector
from os.path import join

from loading_variables import   final_csvs_dir,     \
                                countries_csv,      \
                                stats_csv,          \
                                indicators_csv

cnx = None
cursor = None

def connect():
    global cnx
    global cursor
    
    print('Connecting... ', end=' ')
    try:
        cnx = mysql.connector.connect( host = '127.0.0.1',
                            user = 'root', 
                            password = 'root',
                            allow_local_infile=True)
        cursor = cnx.cursor()
    except mysql.connector.Error as e:
            print(e)
            print("Connection not established.")
    
    print('Done')


def create_database():
    cursor.execute('DROP DATABASE dbms')
    print('Creating database...', end=' ')
    cursor.execute('CREATE DATABASE IF NOT EXISTS dbms')
    cursor.execute('USE dbms')
    print('Done')

def get_headers():
    with open(join(final_csvs_dir, stats_csv), newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        formatted_headers =  [header.replace('.', '_').lower() for header in headers]
        return formatted_headers[2:]

def create_tables():
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
        create_stats_table_query += ',\n %s DOUBLE' % (header)
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

def create_load_query(csv_file, table_name):
    return  """
            LOAD DATA LOCAL INFILE '%s'
            INTO TABLE %s 
            FIELDS TERMINATED BY ','
            OPTIONALLY ENCLOSED BY '"'
            LINES TERMINATED BY '\r\n'
            IGNORE 1 LINES
        """ % (join(final_csvs_dir, csv_file).replace('\\', '/'), table_name)

def load_csvs():
    print('Loading files...', end=' ')
    cursor.execute('SET GLOBAL local_infile=\'ON\';')

    cursor.execute(create_load_query(countries_csv, 'Countries'))
    cursor.execute(create_load_query(stats_csv, 'Stats'))
    cursor.execute(create_load_query(indicators_csv, 'Indicators'))

    print('Done')

def main():
    connect()
    create_database()
    create_tables()
    load_csvs()

    cnx.commit()
    cnx.close()

main()