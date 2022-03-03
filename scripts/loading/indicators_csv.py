import pandas as pd
import numpy as np
import os


class Indicator:
    def __init__(self,cCode,iCode,iName,srcNote,srcOrg):
        self.cCode=cCode #country code
        self.iCode=iCode #indicator code
        self.iName=iName #indicator name
        self.srcNote=srcNote 
        self.srcOrg=srcOrg

        


def create_final_csv():
    data_filepath = 'C:\\Users\\verpc\\Desktop\\DBMS\\csvs\\indicators\\'
    final_df = pd.DataFrame()
    

    for filename in os.listdir(data_filepath):
        df = pd.read_csv(data_filepath + filename)
        filenameSplit=filename.split("_")
        cCode=filenameSplit[3]
        ind = Indicator(cCode,df.loc[0][0], df.loc[0][1],df.loc[0][2], df.loc[0][3])
        
        df.insert(0,"Country Code",[cCode for i in range(0, len(df.index))])
        print(df)
        final_df = pd.concat([final_df, df])

    final_df.to_csv('final_Ind.csv', na_rep='NULL', index = False)

create_final_csv()