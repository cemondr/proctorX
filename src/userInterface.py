#!/usr/bin/env python


from PyQt5.QtWidgets import * 
import sys
import os
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5 import QtCore
from manager import manager
from fileIO import fileInputOutput
from visualizer import trackDataVisualizer

programManager = manager("logs/currentProcesses.txt", "logs/currentTrackedData.txt")
myReader = fileInputOutput("logs/currentProcesses.txt", "logs/currentTrackedData.txt")
myVisualizer = trackDataVisualizer()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "ProctorX"
        self.top = 100
        self.left = 200
        self.width = 300
        self.height = 250

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icons/fs.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: black;")

        self.mainLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def mainLayout(self):

        self.isRunning = False
        self.groupBox = QGroupBox("Main Options")
        self.groupBox.setStyleSheet("border: black;")
        hboxlayout = QHBoxLayout()

        self.runButton = QPushButton("Start",self)
        #runButton.setGeometry(QRect(100,100,150,150))
        self.runButton.setIcon(QtGui.QIcon("icons/play2.png"))
        self.runButton.setStyleSheet("color: white;")
        self.runButton.setIconSize(QtCore.QSize(40,40))
        self.runButton.setMinimumHeight(40)
        self.runButton.clicked.connect(self.callStart)
        hboxlayout.addWidget(self.runButton)

        stopButton = QPushButton("Stop",self)
        #stopButton.setGeometry(QRect(100,100,150,150))
        stopButton.setIcon(QtGui.QIcon("icons/pause.png"))
        stopButton.setStyleSheet("color: white;")
        stopButton.setIconSize(QtCore.QSize(20,25))
        stopButton.setMinimumHeight(40)
        stopButton.clicked.connect(self.callStop)
        hboxlayout.addWidget(stopButton)

        trackedButton = QPushButton("Tracked",self)
        #stopButton.setGeometry(QRect(100,100,150,150))
        trackedButton.setIcon(QtGui.QIcon("icons/track.jpg"))
        trackedButton.setStyleSheet("color: white;")
        trackedButton.setIconSize(QtCore.QSize(40,40))
        trackedButton.setMinimumHeight(40)
        trackedButton.clicked.connect(self.moveToTracked)
        hboxlayout.addWidget(trackedButton)

        dataButton = QPushButton("Data",self)
        #stopButton.setGeometry(QRect(100,100,150,150))
        dataButton.setIcon(QtGui.QIcon("icons/data.jpg"))
        dataButton.setStyleSheet("color: white;")
        dataButton.setIconSize(QtCore.QSize(40,40))
        dataButton.setMinimumHeight(40)
        dataButton.clicked.connect(self.moveToVisualize)
        hboxlayout.addWidget(dataButton)

        self.groupBox.setLayout(hboxlayout)
    
    def moveToTracked(self):
        self.close()
        self.tracked = TrackedWindow()
    
    def moveToVisualize(self):
        self.close()
        self.visualized = visualizer()
    
    def callStart(self):
        self.runButton.setIcon(QtGui.QIcon("icons/redot.JPG"))
        QApplication.processEvents()
        programManager.startrecording()
        self.isRunning = True
    
    def callStop(self):
        programManager.stoprecording()
        self.runButton.setIcon(QtGui.QIcon("icons/play2.png"))
        QApplication.processEvents()
        
    
class TrackedWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "ProctorX"
        self.top = 100
        self.left = 200
        self.width = 850
        self.height = 550

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icons/fs.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: black;")

        self.mainLayout()
        #vbox = QVBoxLayout()
        #vbox.addWidget(self.groupBox)
        #self.setLayout(vbox)
        self.show()
    
    def getTrackedData(self,port):
        currentList = myReader.getAllTrackedLines()
        if(len(currentList)<1):
            return
        bigString = ""
        if (port == 1):
            bigString = "NAME\n"
        elif(port == 0):
            bigString ="TRACK STATUS\n"
        elif(port == 2):
            bigString = "CURRENT TOTAL\n"
            
        
        for line in currentList:
            lineArr = line.split("|")        
            bigString+=lineArr[port]
            if(port != 2):
                bigString+= "\n"
            
        
        return bigString

    def reSetScreen(self):
        nameTrack = self.getTrackedData(1)
        self.displayBox1.setText(nameTrack)
        self.setReset(nameTrack)


        statTrack = self.getTrackedData(0)
        self.displayBox0.setText(statTrack)

        dataTrack = self.getTrackedData(2)
        self.displayBox2.setText(dataTrack)

        QApplication.processEvents()
    
    def pushProcesses(self):
        
        self.displayProcess = QTextEdit()
        self.displayProcess.setReadOnly(True)
        
        thelist = myReader.getAllProcesses()
        oneString = ""
        for x in thelist:
            oneString = oneString + x

        self.displayProcess.setText(oneString)
        self.displayProcess.setFont(self.font)
        self.displayProcess.setStyleSheet("color:green;")
       

        self.hboxlayout.takeAt(0)
        self.hboxlayout.takeAt(0)
        self.hboxlayout.takeAt(0)
        self.hboxlayout.takeAt(0)
        self.hboxlayout.addWidget(self.displayProcess)
        self.dataViewButton.clicked.connect(self.pushBackTrackList)



 
        self.processViewButton.setIcon(QtGui.QIcon("icons/redot.JPG"))
        self.dataViewButton.setIcon(QtGui.QIcon("icons/target.jpg"))
        QApplication.processEvents()
    
    def setReset(self,trackData):
        if(len(trackData)<1):
            return
        tracklist = trackData.split("\n")
     
        self.resetname = "LAST RESET\n"
        for each in tracklist:
            if(len(each)>0 and each != "NAME"):
                self.resetname += myReader.getResetDate(each)
        
        self.displayBox4.setText(self.resetname)


    def pushBackTrackList(self):
        self.close()
        self.tracked = TrackedWindow()

    def firstTexter(self):
        self.hboxlayout = QHBoxLayout()
        self.font = QtGui.QFont()
        self.font.setFamily("Courier")

        self.displayBox4 = QTextEdit()
        self.displayBox4.setFont(self.font)
        self.displayBox4.setStyleSheet("color: green;")
        self.displayBox4.setReadOnly(True)


        self.displayBox1 = QTextEdit()
        trackData = self.getTrackedData(1)
        self.displayBox1.setText(trackData)
        self.displayBox1.setFont(self.font)
        self.displayBox1.setStyleSheet("color: green;")
        self.displayBox1.setReadOnly(True)
        self.hboxlayout.addWidget(self.displayBox1)

        if(trackData):
            self.setReset(trackData)

        self.displayBox0 = QTextEdit()
        trackData = self.getTrackedData(0)
        self.displayBox0.setText(trackData)
        self.displayBox0.setFont(self.font)
        self.displayBox0.setStyleSheet("color: green;")
        self.displayBox0.setReadOnly(True)
        self.hboxlayout.addWidget(self.displayBox0)

        self.displayBox2 = QTextEdit()
        trackData = self.getTrackedData(2)
        self.displayBox2.setText(trackData)
        self.displayBox2.setFont(self.font)
        self.displayBox2.setStyleSheet("color: green;")
        self.displayBox2.setReadOnly(True)
        self.hboxlayout.addWidget(self.displayBox2)
        self.hboxlayout.addWidget(self.displayBox4)

        

    def mainLayout(self):

        self.switchBox=QGroupBox()
        self.switchBox.setStyleSheet("border: 1px solid black;")
        self.switchHorizontal = QHBoxLayout()
        self.dataViewButton= QPushButton("Tracked")
        self.dataViewButton.setStyleSheet("color:white;")
        self.dataViewButton.setIcon(QtGui.QIcon("icons/redot.JPG"))
        
        self.processViewButton = QPushButton("Processes")
        self.processViewButton.setStyleSheet("color:white;")
        self.processViewButton.setIcon(QtGui.QIcon("icons/target.jpg"))
        self.processViewButton.clicked.connect(self.pushProcesses)

        self.switchHorizontal.addWidget(self.dataViewButton)
        self.switchHorizontal.addWidget(self.processViewButton)

        self.switchBox.setLayout(self.switchHorizontal)


        hboxlayout2 = QHBoxLayout()
        vboxlayout = QVBoxLayout()

        self.groupBox = QGridLayout()
        self.groupBox.setSpacing(10)
        self.groupBox.addWidget(self.switchBox)



        self.DisplayGroup = QGroupBox()
        self.EditGroup = QGroupBox()
        
        
        self.firstTexter()
        self.DisplayGroup.setLayout(self.hboxlayout)
        self.groupBox.addWidget(self.DisplayGroup)
        

        self.editable = QLineEdit()
        self.editable.setStyleSheet("color:green; border: 1px solid white;")
        editableLayout = QHBoxLayout()
        editableLayout.addWidget(self.editable)
        vboxlayout.addLayout(editableLayout)

        addButton = QPushButton("New Trackable")
        addButton.setStyleSheet("color: white;")
        addButton.clicked.connect(self.callAdd)
        addButton.clicked.connect(self.reSetScreen)
        hboxlayout2.addWidget(addButton)
        reTrackButton = QPushButton("Retrack")
        reTrackButton.setStyleSheet("color: white;")
        reTrackButton.clicked.connect(self.callTrack)
        reTrackButton.clicked.connect(self.reSetScreen)
        hboxlayout2.addWidget(reTrackButton)
        unTrackButton= QPushButton("UnTrack")
        unTrackButton.setStyleSheet("color: white;")
        unTrackButton.clicked.connect(self.callUntrack)
        unTrackButton.clicked.connect(self.reSetScreen)
        hboxlayout2.addWidget(unTrackButton)
        vboxlayout.addLayout(hboxlayout2)
        resetDataButton = QPushButton("Reset")
        resetDataButton.setStyleSheet("color: white;")
        resetDataButton.clicked.connect(self.callResetData)
        resetDataButton.clicked.connect(self.reSetScreen)
        hboxlayout2.addWidget(resetDataButton)

        self.EditGroup.setLayout(vboxlayout)
        self.EditGroup.setStyleSheet("border: 1px solid black;")
        self.groupBox.addWidget(self.EditGroup)

        dataButton = QPushButton("Home",self)
        #stopButton.setGeometry(QRect(100,100,150,150))
        dataButton.setIcon(QtGui.QIcon("icons/data.jpg"))
        dataButton.setStyleSheet("color: white;")
        dataButton.setIconSize(QtCore.QSize(30,35))
        dataButton.clicked.connect(self.goBackHome)
        dataButton.setMinimumHeight(40)
        self.groupBox.addWidget(dataButton)

        self.setLayout(self.groupBox)
        
        #self.groupBox.setLayout(hboxlayout)
        #self.groupBox.setLayout(hboxlayout2)
    

    #def updateScreen(self):

    def callAdd(self):
        arg = self.editable.text()
        programManager.addNewTrackable(arg)
    
    def callResetData(self):
        arg = self.editable.text()
        programManager.resetData(arg)
        myReader.newReset(arg)

    def callTrack(self):
        arg = self.editable.text()
        programManager.setTrackable(arg)
    
    def callUntrack(self):
        arg = self.editable.text()
        programManager.setUntrackable(arg)

    def goBackHome(self):
        self.close()
        self.home = Window()

class visualizer (QWidget):
    def __init__(self):
        super().__init__()
        self.title = "ProctorX"
        self.top = 100
        self.left = 200
        self.width = 350
        self.height = 550

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icons/fs.png"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: black;")

        self.mainLayout()
        #vbox = QVBoxLayout()
        #vbox.addWidget(self.groupBox)
        #self.setLayout(vbox)
        self.show()
    
    def mainLayout(self):
        index = 0
        self.allcheckboxes =[]
        self.checkBoxScreen = QGroupBox("Check Applications you want to include in the plot")
        self.checkBoxScreen.setStyleSheet("color: white; background-color: 221F1F")
        checkBoxVertical1 = QVBoxLayout()
        checkBoxVertical2 = QVBoxLayout()
        checkBoxHorizontalView = QHBoxLayout()


        self.buttonsScreen = QGroupBox()
        dataButtonsHorizontal = QHBoxLayout()
        homeButtonHorizontal = QHBoxLayout()
        allButtonsVertical =QVBoxLayout()

        self.pageLayout = QGridLayout()

        currentData = myReader.getAllTrackedLines()
        dataSize = len(currentData)

        for piece in currentData:
            pieceArray = piece.split("|")
            temp = QCheckBox(pieceArray[1])
            temp.setStyleSheet("spacing:2px;")
            temp.setStyleSheet("padding-top:100;")
            temp.setIcon(QtGui.QIcon("icons/bal.jpg"))
            temp.setStyleSheet("background-color: blackS; color:mediumvioletred;")
            temp.setIconSize(QtCore.QSize(10,10))
            self.allcheckboxes.append(temp)

            if(index % 2 == 0):
                checkBoxVertical1.addWidget(temp)
            else:
                checkBoxVertical2.addWidget(temp)
            
            index = index +1
        
        checkBoxHorizontalView.addLayout(checkBoxVertical1)
        checkBoxHorizontalView.addLayout(checkBoxVertical2)

        self.checkBoxScreen.setLayout(checkBoxHorizontalView)

        
        pieButton= QPushButton("Show As Pie",self)
        pieButton.setStyleSheet("color:white;")
        pieButton.clicked.connect(self.callMakePie)
        dataButtonsHorizontal.addWidget(pieButton)

        barButton = QPushButton("Show As Bar",self)
        barButton.setStyleSheet("color:white;")
        barButton.clicked.connect(self.callMakeChart)
        dataButtonsHorizontal.addWidget(barButton)
            

        dataButton = QPushButton("Home",self)
        dataButton.setIcon(QtGui.QIcon("icons/data.jpg"))
        dataButton.setStyleSheet("color: white;")
        dataButton.setIconSize(QtCore.QSize(30,35))
        dataButton.clicked.connect(self.goBackHome)
        dataButton.setMinimumHeight(40)
        homeButtonHorizontal.addWidget(dataButton)
        QApplication.setStyle('cleanlooks')


        allButtonsVertical.addLayout(dataButtonsHorizontal)
        allButtonsVertical.addLayout(homeButtonHorizontal)
        self.buttonsScreen.setLayout(allButtonsVertical)
        self.buttonsScreen.setStyleSheet("border: 1px solid black")
    

    
        self.pageLayout.addWidget(self.checkBoxScreen)
        self.pageLayout.addWidget(self.buttonsScreen)

        self.setLayout(self.pageLayout)

    def getCheckedBoxNames(self, boxList):
        nameList = []
        for box in boxList:
            if box.isChecked():
                nameList.append(box.text())
        
        return nameList
    
    def callMakePie(self):
        nameList = self.getCheckedBoxNames(self.allcheckboxes)
        myVisualizer.makeSomePie(nameList)
    
    def callMakeChart(self):
        nameList = self.getCheckedBoxNames(self.allcheckboxes)
        myVisualizer.makeSomeBar(nameList)
    
    def goBackHome(self):
        self.close()
        self.home = Window()

    
myGui = QApplication(sys.argv)
mainWindow = Window()
sys.exit(myGui.exec()) 