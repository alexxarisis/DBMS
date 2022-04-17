# Third party imports
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

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

    def makeTimelinePlot(self, data:TimelineData, years, indicators, perYears):
        plt.figure()
        # Calculate 'buckets'
        if (perYears != 1):
            data, years = self.__getDataByPeriod(data, years, perYears)
        # if its not a string
        if (type(years) != str):
            years = [str(x) for x in years]
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

    def makeScatterPlot(self, data:ScatterData, indicators, countries, perYears):
        plt.figure()
        # Calculate 'buckets'
        if (perYears != 1):
            data.indicator1 = self.__groupValuesMean(data.indicator1, perYears)
            data.indicator2 = self.__groupValuesMean(data.indicator2, perYears)
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

    def __getDataByPeriod(self, data, years, period):
        # data
        for i in range(0, len(data)):
            data[i].values = self.__groupValuesMean(data[i].values, period)

        # years
        years = self.__getYearsByPeriod(years, period)
        
        return data, years

    def __getYearsByPeriod(self, years, period):
        # List containing the new years
        newYears = []
        # Years in periods of 5, 10, etc...
        periods = years[::period]

        # Make the years' labels
        for i in periods:
            newYears.append(str(i) + '-' + str(i+period-1))
        
        # Change the last one if its the same
        if (periods[-1] == years[-1]):
            newYears[-1] = str(periods[-1])
        # or if the label is calculated wrongly
        else:
            newYears[-1] = str(periods[-1]) + '-' + str(years[-1])

        return newYears

    def __groupValuesMean(self, data, period):
        # list containing all the newly calculated values
        newData = []
        # list containing all the values at one period
        sliceData = []

        for i in range(0, len(data)):
            # store every element
            sliceData.append(data[i])

            # if items=period or it is the last batch of items
            if (((i+1) % period) == 0 or (i == (len(data)-1))):
                # Check if all values are None, else
                # calculate the mean of all elements in the list
                if all(x is None for x in sliceData):
                    meanVal = None
                else:
                    meanVal = mean(x for x in sliceData if x is not None)
                # save it
                newData.append(meanVal)
                # reset for the next period's data
                sliceData = []
        return newData