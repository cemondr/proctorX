import time
#a trackable object is formed for each process that is ordered by user to be tracked.

class trackable:
    __name =  None
    __totalSecond = None
    __isTracked = False
    __startTime = 0.0

    def __init__(self,iName, iTotalS):
        self.__name = iName
        self.__totalSecond= iTotalS
        self.__isTracked = False
    
    #Increments the total time the process runs, called when the process is no longer running
    #it has a half a second threshold to avoid incrementing processes that were never running in the first place
    def incrementTotalMs(self,endTime):
        incremental = endTime - (self.__startTime)
        if (incremental > 0.5):
            self.__totalSecond = self.__totalSecond + incremental

    # This is a primer method that logs the start of a process (trackable process gets ready to be tracked)
    def setForTrack(self):
        currentTime = time.time()
        self.__startTime = currentTime
        self.__isTracked = True

    # Trackable process updates time if it is no longer running.
    def setForUpdate(self):
        self.incrementTotalMs(time.time())
        self.resetStartTime()
        self.untrack()
    # Resets the trackable total seconds
    def resetTotalSecond(self):
        self.__totalSecond = 0.0
    
    #Resets the start time
    def resetStartTime (self):
        self.__startTime = 0.0
    
    def getIsTracked(self):
        return self.__isTracked
    
    def getTotalSecond(self):
        return self.__totalSecond
    
    def getName(self):
        return self.__name
    
    def track(self):
        self.__isTracked = True

    def untrack(self):
        self.__isTracked = False