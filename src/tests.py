# dataload
from tests.dataload import (fileInformantTest, 
                            finalCsvWriterTest, 
                            databaseCreatorTest,
                            databaseLoaderTest)
from tests.model import dataFormatterTest

def runDataloadTests():
    fileInfo = fileInformantTest.runTests()
    finalCsvWriterTest.runTests(fileInfo)
    databaseCreatorTest.runTests(fileInfo)
    databaseLoaderTest.runTests(fileInfo)

def runModelTests():
    dataFormatterTest.runTests()

if __name__ == "__main__":
    runDataloadTests()
    runModelTests()