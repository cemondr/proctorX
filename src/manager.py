from recorder import recorder
from threading import Thread
from trackable import trackable
from fileIO import fileInputOutput
import os
import time

class manager:
    __isRecording = False
    __toBeTracked = []
    __myReader = None
    __myRecorder = None


    # might put it in a primer
    def __init__(self,processFilePath,trackFilePath):
        self.__myReader = fileInputOutput(processFilePath,trackFilePath)
        self.__myRecorder = recorder(self.__myReader)
        self.__createTrackableObjects()
        
    #** creates trackable objects from the track data file entries, as long as they are currently set to be tracked!
    def __createTrackableObject(self,line):
        line = line.split("|")
        if(line[0] is 'Y'):
            temp = trackable(line[1],float(line[2]))
            self.__toBeTracked.append(temp)
    
    def __createTrackableObjects(self):
        allAppsInFile = self.__myReader.getAllTrackedLines()
        for line in allAppsInFile:
            self.__createTrackableObject(line)


    # ** Add a new application you want to track to the list of trackables and also into the track file (used as a database). By Default every newly added app is tracked.
    def addNewTrackable(self,newApp):
        toBeAdded = "\nY|"+ newApp +"|0"
        self.__myReader.addNewOnTracked(toBeAdded)
        temp = trackable(newApp,float("0"))
        self.__toBeTracked.append(temp)

    # ** Make a specific application trackable
    def setTrackable(self,appName):
        if(self.__myRecorder.isOn() is True):
            return
        allAppsInFile = self.__myReader.getAllTrackedLines()        
        for i,line in enumerate(allAppsInFile) :
            temp = line.split("|")
            if (temp[1] == appName):
                line = 'Y|'+appName+"|"+temp[2]
                allAppsInFile[i] = line
        self.__myReader.overWriteTrackedLines(allAppsInFile)        
        self.__toBeTracked.clear()
        self.__createTrackableObjects()

    
    # ** Make a specific application untrackable (Change is made in the database)
    def setUntrackable(self,appName):
        if(self.__myRecorder.isOn() is True):
            return 
        allAppsInFile = self.__myReader.getAllTrackedLines()
        for i,line in enumerate(allAppsInFile):
            temp = line.split("|")
            if (temp[1] == appName):
                line = 'N|'+appName+"|"+temp[2]
                allAppsInFile[i] = line
        self.__myReader.overWriteTrackedLines(allAppsInFile)        
        self.__toBeTracked.clear()
        self.__createTrackableObjects()

    #** initiate the call to the recorder by putting it to the thread
    def startrecording(self):
        print("I am recording...")
        if(self.__myRecorder.isOn() is False):
            for app in self.__toBeTracked: 
                app.setForTrack()

            t = Thread(target = self.__myRecorder.turnOnRecording, name="thread1",args=(self.__toBeTracked,))
            t.start()

    #** Stop the recording 
    def stoprecording(self):
        print("I stopped...")
        if(self.__myRecorder.isOn() is True):
            for app in self.__toBeTracked:
                self.__myReader.getProcesses()
                isRunning = self.__myReader.isAppRunning(app.getName())
                if (isRunning is True and app.getIsTracked() is True):
                    app.setForUpdate()
            
            self.__myRecorder.turnOffRecording()
            time.sleep(0.01)
            self.__updateTimeOnData()

    # This method reorganizes the app data and calls the reader/writer to overwrite the trackData file to reflect changes.
    def __updateTimeOnData(self):
        allAppsInFile = self.__myReader.getAllTrackedLines()
        for i, line in enumerate(allAppsInFile):
            temp = line.split("|")
            trackedIndex = self.__isAppInSession(temp[1])
            if(trackedIndex > -1):
                getThis = self.__toBeTracked[trackedIndex].getTotalSecond()
                allAppsInFile[i] = 'Y|'+temp[1]+'|' + str(self.__toBeTracked[trackedIndex].getTotalSecond())
                if(i+1 != len(allAppsInFile)):
                    allAppsInFile[i] = allAppsInFile[i]+'\n'
        self.__myReader.overWriteTrackedLines(allAppsInFile)
    
    def __isAppInSession(self, appName):
        for i, app in enumerate (self.__toBeTracked):
            if (appName == app.getName()):
                return i
        return -1

    def resetData(self,appName):
        if(self.__myRecorder.isOn() is True):
            return
        allAppsInFile = self.__myReader.getAllTrackedLines()
        for i, line in enumerate(allAppsInFile):
            temp = line.split("|")
            if (temp[1]==appName):
                line = temp[0]+'|'+temp[1]+'|'+'0.0'
                if (i != (len(allAppsInFile)-1)):
                    line = line + '\n'
                allAppsInFile[i] = line
        self.__myReader.overWriteTrackedLines(allAppsInFile)
        self.__createTrackableObjects()

    def printAll(self):
        for x in self.__toBeTracked:
            print(x.getName())
    
    def getTrackedObjects(self):
        return self.__toBeTracked