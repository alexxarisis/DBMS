import csv
from mysql.connector import connect, Error
from os import getcwd
from os.path import join
from pathlib import Path

# Must be with '/' and NOT '\' for the sql statement
inputs_dir = ''

countries_csv = 'countries.csv'
stats_csv = 'stats.csv'
indicators_csv = 'indicators.csv'

def initialize_variables():
    global inputs_dir
    
    # Get to csvs directory
    current_path = Path(getcwd())
    csvs_path = join(current_path.parent.parent.absolute(), 'csvs')
    inputs_dir = join(csvs_path, 'final')

def connect_to_database(cursor):
    cursor.execute('DROP DATABASE dbms')
    print('Creating database...', end=' ')
    cursor.execute('CREATE DATABASE IF NOT EXISTS dbms')
    cursor.execute('USE dbms')
    print('Done')

def get_headers():
    with open(join(inputs_dir, stats_csv), newline='') as f:
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

def create_load_query(csv_file, table_name):
    return  """
            LOAD DATA LOCAL INFILE '%s'
            INTO TABLE %s 
            FIELDS TERMINATED BY ','
            OPTIONALLY ENCLOSED BY '"'
            LINES TERMINATED BY '\r\n'
            IGNORE 1 LINES
        """ % (join(inputs_dir, csv_file).replace('\\', '/'), table_name)

def load_csvs(cursor):
    print('Loading files...', end=' ')
    cursor.execute('SET GLOBAL local_infile=\'ON\';')

    cursor.execute(create_load_query(countries_csv, 'Countries'))
    cursor.execute(create_load_query(stats_csv, 'Stats'))
    cursor.execute(create_load_query(indicators_csv, 'Indicators'))

    print('Done')

def load_files_to_mysql():
    initialize_variables()

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
                load_csvs(cursor)
                connection.commit()
                print('Completed.')

                #cursor.execute('SELECT country_id FROM Countries')
                #print(cursor.fetchall())
                connection.close()
    except Error as e:
        print(e)

load_files_to_mysql()