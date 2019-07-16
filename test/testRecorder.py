import unittest
from src.fileIO import fileInputOutput
from src.recorder import recorder
from src.trackable import trackable
from threading import Thread
import time

class testRecorder(unittest.TestCase):

    def testAllRecorder(self):
        testReader = fileInputOutput("logs/testLogs/testProcesses.txt","logs/testLogs/testTrackedData.txt")
        testRecorder = recorder(testReader)
        testList = []
        testTrackable1 = trackable("testString", 0.0)
        testList.append(testTrackable1)
        testTrackable2 = trackable("python",0.0)
        testList.append(testTrackable2)

        for x in testList:
            x.setForTrack()

        t = Thread(target = testRecorder.turnOnRecording, name = "testthread1",args=(testList,))
        t.start()

        time.sleep(0.05)
        self.assertEqual(testRecorder.isOn(), True)
        testRecorder.turnOffRecording()

        self.assertEqual(testTrackable1.getIsTracked(), False)
        self.assertEqual(testTrackable2.getIsTracked(),True)
        self.assertEqual(testRecorder.isOn(), False)



suite = unittest.TestLoader().loadTestsFromTestCase(testRecorder)
unittest.TextTestRunner(verbosity=2).run(suite)