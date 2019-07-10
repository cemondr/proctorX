import unittest
import time
from fileIO import fileIO

class testFileIO(unittest.TestCase):
    def testGetAllTrackedLines(self):
        testReader = fileIO("processList.txt","test.txt")
        result = testReader.getAllTrackedLines()
        assert len(result) == 4
        

    def testAddNewOnTracked(self):
        testReader = fileIO("processList.txt","testTracked.txt")
        testReader.addNewOnTracked("testString\n")
        result = testReader.getAllTrackedLines()
        assert len(result)== 1
        assert result[0] == "testString\n"
        open("testTracked.txt","w").close()
    

    def testOverWrite(self):
        testReader = fileIO("processList.txt","testTracked.txt")
        testReader.addNewOnTracked("testString1\n")
        result = testReader.getAllTrackedLines()
        assert result[0] == "testString1\n"
        testReader.overWriteTrackedLines("testString2\n")
        result = testReader.getAllTrackedLines()
        assert result[0] == "testString2\n"
        open("testTracked.txt","w").close()

    def testIsAppRunning(self):
        testReader = fileIO("testTracked.txt", "testTracked.txt")
        testReader.addNewOnTracked("testString1\n")
        testReader.addNewOnTracked("testString2\n")
        
        res1 = testReader.isAppRunning("testString1")
        self.assertEqual(res1, True)
        res2 = testReader.isAppRunning("testString2")
        self.assertEquals(res2,True)
        res3 = testReader.isAppRunning("testString3")
        self.assertEqual(res3, False)




suite = unittest.TestLoader().loadTestsFromTestCase(testReader)
unittest.TextTestRunner(verbosity=2).run(suite)
