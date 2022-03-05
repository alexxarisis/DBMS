import csv
import mysql.connector as msql
from mysql.connector import Error
import numpy as np
import pandas as pd
import os

filename = 'countries.csv'
class Countries:
    def __init__(self,country_code, region, incomeg, table_name, special_notes):
        self.country_code = country_code
        self.region = region 
        self.incomeg = incomeg
        self.table_name = table_name
        self.special_notes = special_notes

def create_countries_csv():
    data_path = 'D:\\UOICLASSES\\VASILIADIS\\PROJECT\\DBMS\\csvs\\countries\\'
    global finaldf 
    finaldf = pd.DataFrame()
    total_countries =0

    for filename in os.listdir(data_path):
        df = pd.read_csv(data_path + filename)
        finaldf = pd.concat([finaldf, df], axis=0)
    finaldf = finaldf.drop(['Unnamed: 5', 'Unnamed: 4'], axis =1)
    finaldf = finaldf.reset_index(drop=True)
    finaldf.to_csv('countries.csv', na_rep='NULL', index = False)   
    return finaldf
           

def to_mysql_connection_for_countries():
    try:
        print("Creating database...")
        conn = msql.connect(
            host='localhost', 
            user='root',  
            password='root')
        if(conn.is_connected()):
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE countries")
        print("Countries database has been created successfully!")
    except Error as e:
        print("Error while connecting to MySQL", e)


def create_table_countries(finaldf):
    try:
        conn = msql.connect(
            host='localhost', 
            database = 'countries',
            user='root',  
            password='root',
            allow_local_infile=True)
        
        if(conn.is_connected()):
            cursor = conn.cursor()
            cursor.execute("select database()")
            countries = cursor.fetchone()
            print("You're connected to database: ", countries)
            cursor.execute('DROP TABLE IF EXISTS countries_table;')
            print('Creating table....')
            cursor.execute("CREATE TABLE IF NOT EXISTS countries_table(Country_Code varchar(3), Region varchar(255), IncomeGroup varchar(255), TableName varchar(1000), Special_Notes TEXT)")
            print("Table countries has been created!")
            print("Passing arguments into countries table...")
            cursor.execute("SHOW TABLES FROM countries")
            print(cursor.fetchall())
            cursor.execute('SET GLOBAL local_infile=\'ON\';')
            arguments = "LOAD DATA LOCAL INFILE '"  + filename + """'
                    INTO TABLE countries_table
                    FIELDS TERMINATED BY ','
                    OPTIONALLY ENCLOSED BY '"'
                    IGNORE 1 LINES
                """
            cursor.execute(arguments)
            print("Argument inserted")
            conn.commit()
            print("Argument's passing had been finished!")
            cursor.execute('SELECT * FROM countries_table')
            for row in list(cursor.fetchall()):
                print(row)
    except Error as e:
        print("Error while connecting to MySQL", e) 
create_table_countries(create_countries_csv())
    


