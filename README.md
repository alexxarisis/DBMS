# DBMS

## Description
Visualization of 50 statistics from 25 different countries (source: [WorldBank](http://data.worldbank.org/)).

## Installation (Windows only)
1. Install Python and MySQL 8.0
2. Open a terminal and install the following python packages:
    1. pip install pyqt5
    2. pip install matplotlib
    3. pip install mysql-connector-python
    4. pip install pandas
3. MySQL settings:
    1. Close MySQL service by using the command: net stop MySQL80
    2. Allow hidden files to be visible
    3. Head over to the directory "C:\ProgramData\MySQL\MySQL Server 8.0"
    4. Open the "my.ini" file
    5. Set the field 'secure-file-priv'=""
    6. Start MySQL service by using the command: net start MySQL80

## How to run
1. Clone the repository
2. Go to "../DBMS/src/settings.py" and change the database fields to your settings. 
3. Enter the "../DBMS/src/" directory
4. Run main.py

If everything is setup well, a window will pop up.  
Go to 'Application' below.

## How to run tests
1. Do the above steps except #4.
4. Run tests.py
5. If everything is setup well, no errors will be thrown.

## Application
You are now presented with 4 different categories:
* Indicators
* Years
* Countries
* Plots

There are 3 kinds of plots, each working under different conditions (for k,k'>0):

| Plot | # of Indicators | # of Countries | Years Range | Time Aggregation |
| :---: | :-------: | :-------: | :---: | :--------------: |
| Timeline | k | k' | Any | Yes |
| Bar | k | k' | Any | Yes |
| Scatter | 2 | 0 | Specific year | No |
| Scatter | 2 | 1 | Any | Yes |

## How to add more data
1. Go to [WorldBank](http://data.worldbank.org/)
2. Download a .zip file for the country you want.
3. Extract it into 3 files and save each on the corresponding folder in "../DBMS/data/original/":
    1. "countries/"
    2. "indicators/"
    3. "stats"
4. The new files will be loaded along with the old ones when the app is run.

## Credits
Alexandros Charisis
Konstantinos Zioudas
Dimitris Vampiris