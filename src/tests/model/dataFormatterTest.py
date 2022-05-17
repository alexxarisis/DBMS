# Third party imports
import pandas as pd
import mysql.connector
# Local application imports
from model.databaseConnector import DatabaseConnector
from model.dataFormatter import DataFormatter
def runTests():
    
    barform1=DataFormatter().getBarOrTimelineData(["Taxes on exports (current LCU)"],["Angola"],2005,2010,1)
    scatterform1=DataFormatter().getScatterData(["Access to electricity, rural (% of rural population)","Access to electricity, urban (% of urban population)"],["Angola"],2005,2010,1)#todo vale tis xores
    barform5=DataFormatter().getBarOrTimelineData(["Taxes on exports (current LCU)"],["Angola"],2005,2010,5)
    scatterform5=DataFormatter().getScatterData(["Access to electricity, rural (% of rural population)","Access to electricity, urban (% of urban population)"],["Angola"],2005,2010,5)#todo vale tis xores

   
def  getBarOrTimelineDataTest(barform1,barform5):
    df1=pd.DataFrame()
    df5=pd.DataFrame()
    df1["Angola" + ' - ' + "Taxes on exports (current LCU)"]=[144127641.0,86822665.0,71152438.0,9732844.0,7260164.0,10715534.0]
    df1["Years"]=["2005","2006","2007","2008","2009","2010"]
    df5["Angola" + ' - ' + "Taxes on exports (current LCU)"]=[63819150.4,10715534.0]
    df5["Years"]=["2005-2009","2010"]
    assert barform1.equals(df1)== True , "DataFormatter: BarChart or Timeline format wrong "
    assert barform5.equals(df5)== True , "DataFormatter: BarChart or Timeline format wrong "

def getScatterDataTest(scatterform1,scatterform5  ):      
    df1=pd.DataFrame()
    df2=pd.DataFrame()
    df1["Access to electricity, rural (% of rural population)"]=["NaN",9.477077,2.984414 ,2.567459  ,2.019035  ,1.324989 ,0.965577,"NaN",6.609394,"NaN","NaN"] 
    df1["Access to electricity, urban (% of urban population)"]=["NaN", 30.000000,47.587940 ,48.980316,50.385216,51.809338,53.253960
,66.100000,61.310000,  57.668503,73.969627]  
    df2["Access to electricity, rural (% of rural population)"]=[1.324989,92.308199,100.000000 ,100.000000,30.171858,84.830535 , 15.607157 , 88.872906, 88.000751,89.649943,99.097913,100.000000 ,70.715825,100.000000,57.015292,100.000000,100.000000,100.000000,100.000000,100.000000,100.000000,100.000000,89.163561 ,84.502870 ,93.327609   ]  
    df2["Access to electricity, urban (% of urban population)"]=[51.809338,97.382217,100.000000 ,100.000000,82.610000,99.634816 , 80.981430 , 99.300000, 99.625237,99.668752,99.800000,100.000000 ,93.576225,100.000000,91.488167,100.000000,100.000000,100.000000,100.000000,100.000000,100.000000,100.000000,99.449341 ,99.184151 ,99.700363   ]  
    assert scatterform1.equals(df1)== True , "DataFormatter: ScatterData format wrong "
    assert scatterform5.equals(df2)== True , "DataFormatter: ScatterData format wrong "