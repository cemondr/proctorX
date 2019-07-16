import time

class trackable:
    __name =  None
    __totalSecond = None
    __isTracked = False
    __startTime = 0.0

    def __init__(self,iName, iTotalS):
        self.__name = iName
        self.__totalSecond= iTotalS
        self.__isTracked = False
    
    def incrementTotalMs(self,endTime):
        incremental = endTime - (self.__startTime)
        if (incremental > 0.5):
            self.__totalSecond = self.__totalSecond + incremental
    
    def setForTrack(self):
        currentTime = time.time()
        self.__startTime = currentTime
        self.__isTracked = True
    
    def setForUpdate(self):
        self.incrementTotalMs(time.time())
        self.resetStartTime()
        self.untrack()

    def resetTotalSecond(self):
        self.__totalSecond = 0.0
    
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