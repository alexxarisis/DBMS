from os import getcwd
from os.path import join
from pathlib import Path

### CSV'S NAMES ###
countries_csv = 'countries.csv'
stats_csv = 'stats.csv'
indicators_csv = 'indicators.csv'

###########################################
# Get to csv's directory
current_path = Path(getcwd())
csvs_dir = join(current_path.parent.parent.absolute(), 'csvs')

# Input csvs directories
countries_dir = join(csvs_dir, 'countries')
yearly_stats_dir = join(csvs_dir, 'stats')
indicators_dir = join(csvs_dir, 'indicators')

# Output directory
final_csvs_dir = join(csvs_dir, 'final')