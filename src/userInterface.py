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
        hboxlayout.addWidget(trackedButton)

        dataButton = QPushButton("Data",self)
        #stopButton.setGeometry(QRect(100,100,150,150))
        dataButton.setIcon(QtGui.QIcon("icons/data.jpg"))
        dataButton.setStyleSheet("color: white;")
        dataButton.setIconSize(QtCore.QSize(40,40))
        dataButton.setMinimumHeight(40)
        hboxlayout.addWidget(dataButton)

        self.groupBox.setLayout(hboxlayout)
    
    def trackedWindowLayout(self):
        self.title = "ProctorX"
        self.top = 100
        self.left = 200
        self.width = 300
        self.height = 250



    





         


    
    

    def mainButtons(self):
        startRecordingButton = QPushButton("Start",self)
        startRecordingButton.setGeometry(QRect(0,0,75,75))
        startRecordingButton.setFont(self.mainButtonFonts())
        startRecordingButton.setStyleSheet("background-color: blue; border-radius: 36px;")
        stopRecordingButton = QPushButton("Stop",self)
        stopRecordingButton.setGeometry(QRect(0,75,75,75))
        stopRecordingButton.setFont(self.mainButtonFonts())
        stopRecordingButton.setStyleSheet("background-color: red; border-radius: 36px;")

    def mainButtonFonts(self):
        fonts = QtGui.QFont()
        fonts.setFamily("Futura")
        fonts.setPixelSize(11)
        fonts.setBold(False)

        return fonts


myGui = QApplication(sys.argv)
mainWindow = Window()
sys.exit(myGui.exec()) 