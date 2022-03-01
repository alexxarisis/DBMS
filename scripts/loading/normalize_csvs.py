import pandas as pd
import numpy as np
import os

class Country:
    def __init__(self, name, code):
        self.name = name
        self.code = code

def format_dataframe(df):
    # Invert dataframe and drop unnessecary columns
    df = df.T
    df = df.drop(['Country Name', 'Country Code', 'Indicator Name', 'Unnamed: 65'])

    # Name headers based on 'Indicator Code'
    df = df.rename(columns=df.iloc[0]).drop(df.index[0])
    
    # Make years into a column and re-index
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'Year'})    

    # Keep only codes starting with the given strings // ESTW FD & FI
    wanted_columns = ('Year', 'FD', 'FI')
    column_filter = [col for col in df if col.startswith(wanted_columns)]
    return df[column_filter]  

def update_with_country_info_and_unique_IDs(df, total_ids, country):
    total_entries = len(df.index)
    df.insert(0, 'ID', np.arange(total_ids, total_ids + total_entries, 1))
    df.insert(1, 'Country Name', [country.name] * total_entries)
    df.insert(2, 'Country Code', [country.code] * total_entries)

def create_final_csv():
    data_filepath = 'C:\\Users\\alexx\\Desktop\\DBMS\\csvs\\data\\'
    final_df = pd.DataFrame()
    total_ids = 0

    for filename in os.listdir(data_filepath):
        df = pd.read_csv(data_filepath + filename, skiprows=4)
        country = Country(df.loc[0][0], df.loc[0][1])

        df = format_dataframe(df)
        print(df)
        update_with_country_info_and_unique_IDs(df, total_ids, country)

        total_ids = total_ids + len(df.index)
        final_df = pd.concat([final_df, df])

    final_df.to_csv('final.csv', na_rep='NULL', index = False)

create_final_csv()