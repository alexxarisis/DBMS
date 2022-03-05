import pandas as pd
import os

countries_dir = 'C:\\Users\\alexx\\Desktop\\DBMS\\csvs\\countries\\'
yearly_stats_dir = 'C:\\Users\\alexx\\Desktop\\DBMS\\csvs\\data\\'
indicators_dir = 'C:\\Users\\alexx\\Desktop\\DBMS\\csvs\\indicators\\'

output_dir = 'C:\\Users\\alexx\\Desktop\\DBMS\\csvs\\final\\'

# {Country Code: ID}
countryIDs = None

def create_countries_csv():
    global countryIDs
    final_df = pd.DataFrame()

    for filename in os.listdir(countries_dir):
        df = pd.read_csv(countries_dir + filename)
        final_df = pd.concat([final_df, df])

    # Drop unnecessary columns 
    final_df = final_df.drop(['Unnamed: 5', 'Unnamed: 4'], axis=1)
    # Make ID column
    final_df = final_df.reset_index(drop=True)
    final_df.insert(0, 'Country ID', final_df.index)
    
    final_df.to_csv(output_dir + 'countries.csv', na_rep='NULL', index = False)

    # Fill dict with {country-id} values
    countryIDs = dict(zip(final_df['Country Code'], final_df['Country ID']))

def create_yearly_stats_csv():
    global countryIDs
    final_df = pd.DataFrame()

    for filename in os.listdir(yearly_stats_dir):
        df = pd.read_csv(yearly_stats_dir + filename, skiprows=4)

        # Get specific ID of country
        code = df['Country Code'].drop_duplicates().loc[0]
        id = countryIDs.get(code)

        # Invert dataframe and drop unnessecary columns
        df = df.T
        df = df.drop(['Country Name', 'Country Code', 'Indicator Name', 'Unnamed: 65'])

        # Name headers based on 'Indicator Code'
        df = df.rename(columns=df.iloc[0]).drop(df.index[0])
        
        # Make Years from index to a column
        df = df.reset_index()
        df = df.rename(columns={'index': 'Year'})

        # Keep only codes starting with the given strings // ESTW FD & FI
        wanted_columns = ('Year', 'FD', 'FI')
        column_filter = [col for col in df if col.startswith(wanted_columns)]
        df = df[column_filter]

        # insert ID column
        df.insert(0, 'Country ID', id)
        
        final_df = pd.concat([final_df, df])

    final_df.to_csv(output_dir + 'stats.csv', na_rep='NULL', index = False)

def create_indicators_csv():
    final_df = pd.DataFrame()

    for filename in os.listdir(indicators_dir):
        df = pd.read_csv(indicators_dir + filename)
        df = df.drop(['Unnamed: 4'], axis = 1)
        final_df = pd.concat([final_df, df])

    final_df = final_df.drop_duplicates()
    # Make IDs
    final_df = final_df.reset_index()
    final_df = final_df.rename(columns={'index': 'Indicator ID'})
    
    final_df.to_csv(output_dir + 'indicators.csv', na_rep='NULL', index = False)

def create_csvs():
    print('Creating csv\'s...', end=" ")

    create_countries_csv()
    create_yearly_stats_csv()
    create_indicators_csv()

    print('Done')

create_csvs()