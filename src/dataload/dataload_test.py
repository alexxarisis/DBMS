import databaseLoader ,databaseCreator
import unittest   # The test framework

class Test_Dataload(unittest.TestCase):
    def test_dbLoader_connect(self):
        
        self.assertEqual(databaseLoader.__connect(self), 1)

    def test_dbLoader_loadCsvs(self):
        self.assertEqual(databaseLoader.__loadCsvs(self), 1)
    def test_dbLoader_loadCsv(self):
        #TODO: a way to test this
        self.assertEqual(databaseLoader.__loadCsv(self), 1)
        
class Test_Database(unitest.TestCase):
    def test_dbCreator_connect(self):
        
        self.assertEqual(databaseCreator.__connect(self), 1)

    



if __name__ == '__main__':
    unittest.main()