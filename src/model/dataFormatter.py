from statistics import mean

# Local application imports
from model.databaseConnector import DatabaseConnector

class TimelineData():
    def __init__(self, country, indicator, values):
        self.name = country + ' - ' + indicator
        self.values = values

class ScatterData():
    def __init__(self, data):
        self.indicator1 = data[0]
        self.indicator2 = data[1]

class DataFormatter():
    def __init__(self):
        self.dbConnector = DatabaseConnector()

    # Returns a list of TimelineData objects
    def getTimelineData(self, indicators, countries, fromYear, toYear, perYears):
        # List containing all the TimelineData objects
        data = []
        for indicator in indicators:
            for country in countries:
                values = self.dbConnector.selectBasedOnMultipleVariables(
                            indicator, country, fromYear, toYear)
                data.append(TimelineData(country, indicator, values))
        
        # Calculate buckets of data, get average for each
        if (perYears != 1):
            for i in range(0, len(data)):
                data[i].values = self.__groupValuesMean(data[i].values, perYears)
        return data

    # Returns a ScatterData object
    def getScatterData(self, indicators, countries, fromYear, toYear, perYears):
        # List containing  all the data values
        data = []
        for indicator in indicators:
            # Option done by user, choose data accordingly
            if (fromYear == toYear):
                data.append(self.dbConnector.
                    selectBasedOnYear(indicator, fromYear))
            else:
                data.append(self.dbConnector.selectBasedOnMultipleVariables(
                    indicator, countries[0], fromYear, toYear))

        # Calculate buckets of data, get average for each
        if (perYears != 1):
            data[0] = self.__groupValuesMean(data[0], perYears)
            data[1] = self.__groupValuesMean(data[1], perYears)
        
        return ScatterData(data)

    def getYearsByPeriod(self, years, period):
        # Return it as string, if no changes needed
        if (period == 1):
            return [str(x) for x in years]

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