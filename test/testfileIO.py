import unittest
import time
from src.fileIO import fileInputOutput
class testFileIO(unittest.TestCase):
    def testGetAllTrackedLines(self):
        testReader = fileInputOutput("logs/testLogs/testProcesses.txt","logs/testLogs/testTrackedData.txt")
        testReader.addNewOnTracked("entry1\n")
        testReader.addNewOnTracked("entry2\n")
        testReader.addNewOnTracked("entry3\n")
        testReader.addNewOnTracked("entry4")
        result = testReader.getAllTrackedLines()
        assert len(result) == 4
        open("logs/testLogs/testTrackedData.txt","w").close()

        

    def testAddNewOnTracked(self):
        testReader = fileInputOutput("logs/testLogs/testProcesses.txt","logs/testLogs/testTrackedData.txt")
        testReader.addNewOnTracked("testString\n")
        result = testReader.getAllTrackedLines()
        assert len(result)== 1
        assert result[0] == "testString\n"
        open("logs/testLogs/testTrackedData.txt","w").close()
    

    def testOverWrite(self):
        testReader = fileInputOutput("logs/testLogs/testProcesses.txt","logs/testLogs/testTrackedData.txt")
        testReader.addNewOnTracked("testString1\n")
        result = testReader.getAllTrackedLines()
        assert result[0] == "testString1\n"
        testReader.overWriteTrackedLines("testString2\n")
        result = testReader.getAllTrackedLines()
        assert result[0] == "testString2\n"
        open("logs/testLogs/testTrackedData.txt","w").close()

    def testIsAppRunning(self):
        testReader = fileInputOutput("logs/testLogs/testProcesses.txt","logs/testLogs/testTrackedData.txt")
        
        res1 = testReader.isAppRunning("firefox")
        self.assertEqual(res1, True)
        res2 = testReader.isAppRunning("code")
        self.assertEqual(res2,True)
        res3 = testReader.isAppRunning("safari")
        self.assertEqual(res3, False)




suite = unittest.TestLoader().loadTestsFromTestCase(testFileIO)
unittest.TextTestRunner(verbosity=2).run(suite)
