import csv
from mysql.connector import connect, Error
from os.path import join

from loading_variables import final_csvs_dir
from loading_variables import countries_csv
from loading_variables import stats_csv
from loading_variables import indicators_csv

def connect_to_database(cursor):
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

def load_csvs(cursor):
    print('Loading files...', end=' ')
    cursor.execute('SET GLOBAL local_infile=\'ON\';')

    cursor.execute(create_load_query(countries_csv, 'Countries'))
    cursor.execute(create_load_query(stats_csv, 'Stats'))
    cursor.execute(create_load_query(indicators_csv, 'Indicators'))

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
                load_csvs(cursor)
                connection.commit()
                print('Completed.')

                #cursor.execute('SELECT country_id FROM Countries')
                #print(cursor.fetchall())
                connection.close()
    except Error as e:
        print(e)

load_files_to_mysql()