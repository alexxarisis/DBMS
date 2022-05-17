from dataload.fileInformant import DBCreator

import mysql.connector

def runTests(fileInfo):
    DBCreator(fileInfo).createDB()
    
    cnx, cursor = connect()

def connect():
    try:
        cnx = mysql.connector.connect( host = '127.0.0.1',
                            user = 'root', 
                            password = 'root')
        cursor = cnx.cursor()
    except mysql.connector.Error as e:
            print(e)
            print("DBCreatorTst: Connection not established.")
    return cnx, cursor

def test():
    print()
# na dw ta trapezia an uparxoun kai ti exoun san pedia