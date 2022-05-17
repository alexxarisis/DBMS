# dataload
from tests.dataload import fileInformantTest
from tests.dataload import finalCsvWriterTest

## dataload tests
fileInfo = fileInformantTest.runTests()
finalCsvWriterTest.runTests(fileInfo)