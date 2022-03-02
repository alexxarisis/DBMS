import csv
from mysql.connector import connect, Error
#from getpass import getpass

filename = 'final.csv'
filename2 = 'final_Ind.csv'

def connect_to_database(cursor):
    print('Creating database...', end=' ')
    cursor.execute('CREATE DATABASE IF NOT EXISTS dbms')
    cursor.execute('USE dbms')
    print('Done')

def get_headers():
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        formatted_headers =  [header.replace('.', '_').lower() for header in headers]
        return formatted_headers[4:]

def get_headers2():
    with open(filename2, newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        formatted_headers =  [header.replace('.', '_').lower() for header in headers]
        return formatted_headers[4:]

def create_table(cursor):
    print('Creating tables...', end=' ')
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS data(
            id INT NOT NULL,
            country_name VARCHAR(64),
            country_code VARCHAR(3),
            year YEAR NOT NULL,
            PRIMARY KEY (id, year)'''
            

    for header in get_headers():
        create_table_query += ', \n' + header + ' DOUBLE'
    create_table_query += ')'

    cursor.execute(create_table_query)
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS indicators(
            country_code VARCHAR(3),
            indicator_code VARCHAR(32),
            indicator_name VARCHAR(70),
            source_note VARCHAR(130),
            source_org VARCHAR(32),
            PRIMARY KEY indicator_code'''
            

    for header in get_headers2():
        create_table_query += ', \n' + header + ' DOUBLE'
    create_table_query += ')'

    cursor.execute(create_table_query)
    print('Done')

def load_csv(cursor):
    print('Loading files...', end=' ')
    cursor.execute('SET GLOBAL local_infile=\'ON\';')

    load_query = "LOAD DATA LOCAL INFILE '"  + filename + """'
        INTO TABLE data
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        IGNORE 1 LINES
    """
    
    cursor.execute(load_query)
    load_query = "LOAD DATA LOCAL INFILE '"  + filename2 + """'
        INTO TABLE indicators
        FIELDS TERMINATED BY ','
        OPTIONALLY ENCLOSED BY '"'
        IGNORE 1 LINES
    """
    
    cursor.execute(load_query)
    print('Done')

def connect_to_mysql():
    try:
        with connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            # user=input('Enter username: '),
            # password=getpass('Enter password: ')
            allow_local_infile=True
        ) as connection:
            with connection.cursor() as cursor:
                connect_to_database(cursor)
                create_table(cursor)
                load_csv(cursor)
                connection.commit()
                print('Completed')

                #cursor.execute('SELECT * FROM data')
                #for row in list(cursor.fetchall()):
                #    print(row)
    except Error as e:
        connection.close()

connect_to_mysql()