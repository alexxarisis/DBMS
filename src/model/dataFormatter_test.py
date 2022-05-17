import dataFormatter
import unittest
import pandas as pd
import numpy as np

from model.dataFormatter import DataFormatter   # The test framework
df = DataFormatter()


#data_1 = {'product_1': ['computer','monitor','printer','desk'],
 #                  'price_1': [1200,800,200,350]
  #                 }
#df1 = pd.DataFrame(data_1)


#data_2 = {'product_2': ['computer','monitor','printer','desk'],
        #            'price_2': [900,800,300,350]
          #          }
#df2 = pd.DataFrame(data_2)


#df1['price_2'] = df2['price_2'] #add the price_2 column from df2 to df1
#df1['prices_match'] = np.where(df1['price_1'] == df2['price_2'], 'True', 'False') #create a new column in df1 to check if prices match

#print(df1)

class Test_DataFormatter(unittest.TestCase):
    def test_dbLoader_connect(self):
        
        self.assertEqual(1, 1)

    def test_dbLoader_loadCsvs(self):
        self.assertEqual(1, 1)
    def test_dbLoader_loadCsv(self):
        #TODO: a way to test this
        self.assertEqual(1, 1)
        


    



if __name__ == '__main__':
    unittest.main()