# Standard library imports
from os.path import join

# Third party imports
import mysql.connector
import pandas as pd

# Local application imports
from dataload.databaseCreator import DBCreator

def runTests(fileInfo):
    DBCreator(fileInfo).createDB()
    
    cnx, cursor = connect()
    tablesCreatedTest(cursor)
    countriesTableTest(cursor)
    indicatorsTableTest(cursor)
    statsTableTest(fileInfo, cursor)

    cnx.close()

def connect():
    try:
        cnx = mysql.connector.connect( host = '127.0.0.1',
                            user = 'root', 
                            password = 'root',
                            database = 'dbms')
        cursor = cnx.cursor()
    except mysql.connector.Error as e:
            print(e)
            print("DBCreatorTest: Connection not established.")
    return cnx, cursor

def tablesCreatedTest(cursor):
    assert findTable(cursor, 'countries') == 1, 'MySQL: countries table is not created'
    assert findTable(cursor, 'indicators') == 1, 'MySQL: indicators table is not created'
    assert findTable(cursor, 'stats') == 1, 'MySQL: stats table is not created'

def findTable(cursor, tablename):
    cursor.execute(
            "SELECT count(*) FROM information_schema.tables "
            "WHERE table_schema = 'dbms' AND "
            "table_name = '%s'" % tablename)
    return cursor.fetchone()[0]

def countriesTableTest(cursor):
    expectedColumnHeaders =  ['country_code', 'region', 'income_group',
                                'country_name', 'special_notes', 'country_id']
    columnHeaders = getTableColumnNames(cursor, 'countries')
    assert columnHeaders == expectedColumnHeaders, 'DBCreator: Countries table has wrong column names'

def indicatorsTableTest(cursor):
    expectedColumnHeaders =  ['indicator_code', 'indicator_name', 'source_note',
                                'source_organization', 'indicator_id']
    columnHeaders = getTableColumnNames(cursor, 'indicators')
    assert columnHeaders == expectedColumnHeaders, 'DBCreator: Indicators table has wrong column names'

def statsTableTest(fileInfo, cursor):
    statsCsv = pd.read_csv(join(fileInfo.outputDir, fileInfo.statsCsv))
    expectedColumnHeaders = [str(x).lower().replace('.', '_').replace(' ', '_') for x in statsCsv.columns]
    columnHeaders = getTableColumnNames(cursor, 'stats')
    assert columnHeaders == expectedColumnHeaders, 'DBCreator: Stats table has wrong column names'

def getTableColumnNames(cursor, tableName):
    cursor.execute(
            "SELECT * "
            "FROM INFORMATION_SCHEMA.COLUMNS "
            "WHERE TABLE_NAME = N'%s'" % tableName)
    return [str(x[3]) for x in cursor.fetchall()]