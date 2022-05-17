# dataload
from tests.dataload import (fileInformantTest, 
                            finalCsvWriterTest, 
                            databaseCreatorTest,
                            databaseLoaderTest)

def runDataloadTests():
    fileInfo = fileInformantTest.runTests()
    finalCsvWriterTest.runTests(fileInfo)
    databaseCreatorTest.runTests(fileInfo)
    databaseLoaderTest.runTests(fileInfo)

if __name__ == "__main__":
    runDataloadTests()