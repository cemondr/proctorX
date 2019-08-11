import os
class fileInputOutput:
    __processFilePath = None
    __trackFilePath = None
    
    # ** Initialize object with a path to the file where the processes will be read
    def __init__(self, iProcessFilePath, iTrackFilePath):
        self.__processFilePath = iProcessFilePath
        self.__trackFilePath = iTrackFilePath
    
    def getProcesses(self):
        command = "ps -Ao comm > "+self.__processFilePath
        os.system(command)


    # ** Check if the App name that is passed as appString is in the processList file, if so return True, otherwise return False
    def isAppRunning(self,appString):
        with open (self.__processFilePath, "r")as myfile:
            processes = myfile.readlines()
        for line in processes:
            if appString in line:
                return True
        return False
    
    # ** Returns all the entries in the tracked applications file (currentTrackedData.txt, for the purposes of this program)
    def getAllTrackedLines(self):
        with open (self.__trackFilePath, "r") as myfile:
            data = myfile.readlines()

        return data
    
    def addNewOnTracked(self,toBeAdded):
        with open (self.__trackFilePath, "a")as myfile:
            myfile.write(toBeAdded)
    
    def overWriteTrackedLines(self,fullData):
        with open(self.__trackFilePath, "w")as myfile:
            myfile.writelines(fullData)
    
    def getAllProcesses(self):
        with open (self.__processFilePath, "r")as myfile:
            processes = myfile.readlines()
        
        return processes



myReader = fileInputOutput("logs/currentProcesses.txt", "logs/currentData.txt")
myReader.getProcesses()