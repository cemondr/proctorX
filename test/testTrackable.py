import unittest
import time
from src.trackable import trackable

class testTrackable(unittest.TestCase):
    def testIncrementTotalMs(self):
        testTrackable = trackable("testTrackable",0.0)
        testTrackable.incrementTotalMs(20.0)
        self.assertEqual(testTrackable.getTotalSecond(),20)
        testTrackable.incrementTotalMs(40.0)
        self.assertEqual(testTrackable.getTotalSecond(),60)
    
    def testSetForTrack(self):
        testTrackable = trackable("testTrackable",0.0)
        testTrackable.setForTrack()
        self.assertEquals(testTrackable.getIsTracked(), True)
        testTrackable.incrementTotalMs(time.time()+3)
        self.assertGreater(testTrackable.getTotalSecond(),0)
    
    def testSetForUpdate(self):
        testTrackable = trackable("testTrackable", 0.0)
        testTrackable.setForUpdate()
        self.assertEquals(testTrackable.getIsTracked(), False)
        self.assertNotEquals(testTrackable.getTotalSecond(), 0.0)    

    def testResetTotalSecond(self):
        testTrackable = trackable("testTrackable", 0.0)
        testTrackable.incrementTotalMs(20.0)
        self.assertEquals(testTrackable.getTotalSecond(),20)
        testTrackable.resetTotalSecond()
        self.assertEquals(testTrackable.getTotalSecond(),0)
    
    def testGetIsTracked(self):
        testTrackable = trackable("testTrackable", 0.0)
        self.assertEquals(testTrackable.getIsTracked(), False)
        testTrackable.track()
        self.assertEquals(testTrackable.getIsTracked(), True)
    
    def testGetName(self):
        testTrackable = trackable("testTrackable", 0.0)
        self.assertEquals(testTrackable.getName(), "testTrackable")





suite = unittest.TestLoader().loadTestsFromTestCase(testTrackable)
unittest.TextTestRunner(verbosity=2).run(suite)