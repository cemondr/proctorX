from PyQt5.QtWidgets import * 
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5 import QtCore
from manager import manager
from fileIO import fileInputOutput

programManager = manager("logs/currentProcesses.txt", "logs/currentTrackedData.txt")
myReader = fileInputOutput("logs/currentProcesses.txt", "logs/currentTrackedData.txt")


class Window(QDialog):
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

        self.groupBox = QGroupBox("Main Options")
        #self.groupBox.setStyleSheet("border: black;")
        hboxlayout = QHBoxLayout()

        runButton = QPushButton("Start",self)
        #runButton.setGeometry(QRect(100,100,150,150))
        runButton.setIcon(QtGui.QIcon("icons/play2.png"))
        runButton.setStyleSheet("color: white;")
        runButton.setIconSize(QtCore.QSize(40,40))
        runButton.setMinimumHeight(40)
        runButton.clicked.connect(programManager.startrecording)
        hboxlayout.addWidget(runButton)

        stopButton = QPushButton("Stop",self)
        #stopButton.setGeometry(QRect(100,100,150,150))
        stopButton.setIcon(QtGui.QIcon("icons/pause.png"))
        stopButton.setStyleSheet("color: white;")
        stopButton.setIconSize(QtCore.QSize(20,25))
        stopButton.setMinimumHeight(40)
        stopButton.clicked.connect(programManager.stoprecording)
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
        hboxlayout.addWidget(dataButton)

        self.groupBox.setLayout(hboxlayout)
    
    def moveToTracked(self):
        self.close()
        self.tracked = TrackedWindow()
    
class TrackedWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "ProctorX"
        self.top = 100
        self.left = 200
        self.width = 650
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


        statTrack = self.getTrackedData(0)
        self.displayBox0.setText(statTrack)

        dataTrack = self.getTrackedData(2)
        self.displayBox2.setText(dataTrack)

        QApplication.processEvents()

    def mainLayout(self):

        hboxlayout2 = QHBoxLayout()
        vboxlayout = QVBoxLayout()

        self.groupBox = QGridLayout()
        self.groupBox.setSpacing(10)
        #self.groupBox.setStyleSheet("border: black;")



        self.DisplayGroup = QGroupBox()
        self.EditGroup = QGroupBox()
        self.hboxlayout = QHBoxLayout()

        self.font = QtGui.QFont()
        self.font.setFamily("Courier")


        self.displayBox1 = QTextEdit()
        trackData = self.getTrackedData(1)
        self.displayBox1.setText(trackData)
        self.displayBox1.setFont(self.font)
        self.displayBox1.setStyleSheet("color: green;")
        self.displayBox1.setReadOnly(True)
        self.hboxlayout.addWidget(self.displayBox1)


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

        self.DisplayGroup.setLayout(self.hboxlayout)
        self.groupBox.addWidget(self.DisplayGroup)
        self.groupBox.setSpacing(10)
        

        self.editable = QLineEdit()
        self.editable.setStyleSheet("color: green;")
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

        self.EditGroup.setLayout(vboxlayout)
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
    
    def callTrack(self):
        arg = self.editable.text()
        programManager.setTrackable(arg)
    
    def callUntrack(self):
        arg = self.editable.text()
        programManager.setUntrackable(arg)

    def goBackHome(self):
        self.close()
        self.home = Window()
    







    





        


myGui = QApplication(sys.argv)
mainWindow = Window()
sys.exit(myGui.exec()) 