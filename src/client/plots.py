from unicodedata import name
import matplotlib.pyplot as plt
import numpy as np

def barChartk(countries,indicator,name,yname):
    y_pos = np.arange(len(countries))
    y_val = []

    plt.bar(y_pos, y_val ,align='center', alpha=0.5)
    plt.xticks(y_pos, countries)
    plt.ylabel(yname)
    plt.title(name)

    plt.show()

def barChartkindk(countries,indicator,name,yname):
    y_pos = np.arange(len(countries))
    y_val = []

    plt.bar(y_pos, y_val ,align='center', alpha=0.5)
    plt.xticks(y_pos, countries)
    plt.ylabel(yname)
    plt.title(name)

    # data set ftiaksimooo
    x = ['A', 'B', 'C', 'D']
    y1 = [100, 120, 110, 130]
    y2 = [120, 125, 115, 125]

    # plot stacked bar chart 
    plt.bar(x, y1, color='g')
    plt.bar(x, y2, bottom=y1, color='y')
    plt.show()


def LineChartk(countries,indicator,name,yname,xname):
    
  
    plt.plot(countries, indicator)
    plt.title(name)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.show()

def LineChartkindk(countries,indicator,name,yname,xname):
    
    #ftiaksimo
    plt.plot(countries, indicator)
    plt.title(name)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.show()

def Scatter2measures(m1 , m2,xname,yname,name):


    # Simple Scatterplot
    
    plt.scatter(m1, m2)
    plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})#???????????
    plt.title(name)
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.show()