import os
import datetime
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
        print(len(toBeAdded))
        if(len(self.getAllTrackedLines())>0):
            toBeAdded = "\n"+toBeAdded
        with open (self.__trackFilePath, "a")as myfile:
            myfile.write(toBeAdded)
    
    def overWriteTrackedLines(self,fullData):
        with open(self.__trackFilePath, "w")as myfile:
            myfile.writelines(fullData)
    
    def getAllProcesses(self):
        self.getProcesses()
        with open (self.__processFilePath, "r")as myfile:
            processes = myfile.readlines()
        
        return processes
    
    def newReset(self,appName):
        if(len(appName)<1):
            return
        dateStr = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        allAppsInFile = self.getAllReset()        
        for i,line in enumerate(allAppsInFile) :
            temp = line.split("|")
            if (temp[0] == appName):
                line =temp[0]+"|"+dateStr+"\n"
                allAppsInFile[i] = line
                self.overWriteResetLines(allAppsInFile)
                return
        
        if(len(allAppsInFile)!=0):
            toBeAdded = "\n"
        else:
            toBeAdded =""
        toBeAdded += appName+"|"+dateStr
        with open("logs/resetDate.txt", "a")as myfile:
            myfile.write(toBeAdded)
        
    def overWriteResetLines(self,fullData):
        with open("logs/resetDate.txt", "w")as myfile:
            myfile.writelines(fullData)
    
    def getAllReset(self):
        with open("logs/resetDate.txt","r") as myfile:
            resets = myfile.readlines()
        
        return resets
    
    def getResetDate(self, appName):
        allAppsInFile = self.getAllReset()
        for i, line in enumerate(allAppsInFile):
            temp = line.split("|")
            if (temp[0]==appName):
                return temp[1]
        
        error = "didn't found\n"
        num = len(allAppsInFile)
        
        return error



myReader = fileInputOutput("logs/currentProcesses.txt", "logs/currentData.txt")
myReader.getProcesses()