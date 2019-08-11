import matplotlib.pyplot as plt
import matplotlib.colors as pltcol
import datetime
from fileIO import fileInputOutput
import numpy as np


class trackDataVisualizer:
    __myreader = fileInputOutput("logs/currentProcesses.txt","logs/currentTrackedData.txt")
    __trackData = []
    __labels = []

    def __init__(self):
        self.primeForAllData()


    def primeForAllData(self):
        data = self.__myreader.getAllTrackedLines()
        del self.__trackData[:] 
        del self.__labels[:] 
        for i, line in enumerate(data):
            temp = line.split("|")
            self.__labels.append(temp[1][15:])
            self.__trackData.append(float(temp[2]))
    
    def primeForSomeData(self,userList):
        data = self.__myreader.getAllTrackedLines()
        del self.__trackData[:]
        del self.__labels[:]
        for i, line in enumerate(data):
           temp =line.split("|")
           if (temp[1] in userList):
               self.__labels.append(temp[1])
               self.__trackData.append(float(temp[2]))

    def displayFields(self):
        print('\n')
        for x in self.__trackData:
            print(x)
        print('\n')
        for y in self.__labels:
            print(y)
        
    def makeAllPie(self):
        self.primeForAllData()
        all_colors = [k for k,v in pltcol.cnames.items()]
        plt.pie(self.__trackData, labels = self.__labels, colors= all_colors ,shadow = False, autopct = '%1.1f%%')  
        plt.axis('equal')
        plt.show() 
    
    def makeSomePie(self,userList):
        self.primeForSomeData(userList)
        plt.ion()
        plt.style.use('dark_background')
        dateStr = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        plt.text(0.07, 1.05,dateStr,fontsize=14, transform=plt.gcf().transFigure)

        all_colors = [k for k,v in pltcol.cnames.items()]
        print("LABEL SIZE: "+ str(len(self.__labels)))
        print("DATA SIZE: " + str(len(self.__trackData)))
        plt.pie(self.__trackData, labels = self.__labels, colors= all_colors ,shadow = False, autopct = '%1.1f%%',textprops={'color': 'b'})  
        plt.text(0.07, 0.05,dateStr,fontsize=14, transform=plt.gcf().transFigure)

        plt.axis('equal')
        plt.show() 
    
    def makeTwoPie(self,a1,a2):
        self.primeForAllData()
        all_colors = [k for k,v in pltcol.cnames.items()]
        label = []
        data = []
        for i, x in enumerate(self.__labels):
            if ((x == a1) or (x == a2)):
                label.append(x)
                data.append(self.__trackData[i])
        
        
        plt.pie(data, labels = label, colors= all_colors ,shadow = False, autopct = '%1.1f%%', ) 
     
 
        plt.axis('equal')
        plt.show() 
    
    #Refactor these
    def makeSomeBar(self,userList):
        self.primeForSomeData(userList)
        plt.ion()
        y_pos = np.arange(len(self.__trackData))
        plt.bar(y_pos, self.__trackData)
        plt.xticks(y_pos, self.__labels)
        dateStr = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        plt.title('Time Ran in Seconds on: ' + dateStr)

        plt.show()

        
    def  makeAllBar(self):
        self.primeForAllData()
        y_pos = np.arange(len(self.__trackData))
        plt.bar(y_pos, self.__trackData)
        plt.xticks(y_pos, self.__labels)
        plt.title('Time Ran in Seconds')
        plt.show()