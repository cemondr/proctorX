from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "ProctorX"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 800
        self.newWindow()

    def newWindow(self):
        self.setWindowIcon(QtGui.QIcon("icons/fs.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.mainButtons()
        self.setStyleSheet("QMainWindow {background-image: url(icons/67878.png); background-attachment: fixed;background-size: cover}")
        self.show()
    

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