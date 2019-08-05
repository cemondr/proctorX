from PyQt5.QtWidgets import * 
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5 import QtCore
from manager import manager

programManager = manager("logs/currentProcesses.txt", "logs/currentTrackedData.txt")


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
    
class TrackedWindow(QDialog):
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

        dataButton = QPushButton("Home",self)
        #stopButton.setGeometry(QRect(100,100,150,150))
        dataButton.setIcon(QtGui.QIcon("icons/data.jpg"))
        dataButton.setStyleSheet("color: white;")
        dataButton.setIconSize(QtCore.QSize(40,40))
        dataButton.clicked.connect(self.goBackHome)
        dataButton.setMinimumHeight(40)
        hboxlayout.addWidget(dataButton)
        
        self.groupBox.setLayout(hboxlayout)

    def goBackHome(self):
        self.close()
        self.home = Window()







    





        


myGui = QApplication(sys.argv)
mainWindow = Window()
sys.exit(myGui.exec()) 