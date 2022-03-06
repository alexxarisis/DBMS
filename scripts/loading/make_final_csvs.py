import pandas as pd
from os import getcwd
from os import listdir
from os.path import join
from pathlib import Path

# Input
countries_dir = ''
yearly_stats_dir = ''
indicators_dir = ''

# Output
output_dir = ''

# {Country Code: ID} dictionary
countryIDs = None

def initialize_variables():
    global countries_dir
    global yearly_stats_dir
    global indicators_dir
    global output_dir

    # Get to csvs directory
    current_path = Path(getcwd())
    csvs_path = join(current_path.parent.parent.absolute(), 'csvs')

    countries_dir = join(csvs_path, 'countries')
    yearly_stats_dir = join(csvs_path, 'stats')
    indicators_dir = join(csvs_path, 'indicators')

    output_dir = join(csvs_path, 'final')

def export_to_csv(df, output_file_name):
    df.to_csv(join(output_dir, output_file_name + '.csv'), na_rep='NULL', index = False)

def create_countries_csv():
    global countryIDs
    final_df = pd.DataFrame()

    for filename in listdir(countries_dir):
        df = pd.read_csv(join(countries_dir, filename))
        final_df = pd.concat([final_df, df])

    # Drop unnecessary columns 
    final_df = final_df.drop(['Unnamed: 5', 'Unnamed: 4'], axis=1)
    # Make ID column
    final_df = final_df.reset_index(drop=True)
    final_df.insert(0, 'Country ID', final_df.index)
    
    export_to_csv(final_df, 'countries')

    # Fill dict with {country-id} values
    countryIDs = dict(zip(final_df['Country Code'], final_df['Country ID']))

def create_yearly_stats_csv():
    global countryIDs
    final_df = pd.DataFrame()

    for filename in listdir(yearly_stats_dir):
        df = pd.read_csv(join(yearly_stats_dir, filename), skiprows=4)

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

    export_to_csv(final_df, 'stats')

def create_indicators_csv():
    final_df = pd.DataFrame()

    for filename in listdir(indicators_dir):
        df = pd.read_csv(join(indicators_dir, filename))
        df = df.drop(['Unnamed: 4'], axis = 1)
        final_df = pd.concat([final_df, df])

    final_df = final_df.drop_duplicates()
    # Make IDs
    final_df = final_df.reset_index()
    final_df = final_df.rename(columns={'index': 'Indicator ID'})
    
    export_to_csv(final_df, 'indicators')

def create_csvs():
    print('Creating csv\'s...', end=" ")

    initialize_variables()
    create_countries_csv()
    create_yearly_stats_csv()
    create_indicators_csv()

    print('Done')

create_csvs()