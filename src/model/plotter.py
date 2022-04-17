# Third party imports
import matplotlib.pyplot as plt
import numpy as np

from model.dataFormatter import TimelineData, ScatterData

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

############################

class PlotMaker:
    def __init__(self):
        plt.ion()

    def makeTimelinePlot(self, data:TimelineData, years, indicators):
        plt.figure()
        # plot
        for i in data:
            plt.plot(years, i.values, label=i.name)

        # THE REST
        # dunno
        # plt.title('\n'.join(indicators), fontsize=8)
        plt.legend(fontsize=8)
        # removes scientific scaling
        plt.ticklabel_format(style='plain', axis='y')
        # numbers fit
        plt.tight_layout()
        plt.show()

    def makeScatterPlot(self, data:ScatterData, indicators, countries):
        plt.figure()
        # plot
        plt.scatter(data.indicator1, data.indicator2)

        # THE REST
        # plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})       #???????????
        plt.xlabel(indicators[0])
        plt.ylabel(indicators[1])
        if (len(countries) == 1):
            plt.title('Correlation of %s' % (countries[0]))
        else:
            plt.title('Correlation of all countries')
        plt.ticklabel_format(style='plain')
        plt.tight_layout()
        plt.show()