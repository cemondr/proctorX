from src.fileIO import fileInputOutput
import time
import os 


class recorder:
    __myreader = None 
    __isRecording  = False

    def __init__(self, iReader):
        self.__isRecording = False
        self.__myreader = iReader
    
    def turnOnRecording(self,currentlyTracked):
        self.__isRecording = True
        while(self.__isRecording is True):
            self.__myreader.getProcesses()
            for app in currentlyTracked:
                isRunning = self.__myreader.isAppRunning(app.getName())
                if ((isRunning is False) and (app.getIsTracked() is True)):
                    app.setForUpdate()
                elif((isRunning is True ) and (app.getIsTracked() is False)):
                    app.setForTrack()

            time.sleep(0.1)

    def turnOffRecording(self):
        self.__isRecording = False
    
    def isOn(self):
        return self.__isRecording