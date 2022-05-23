import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Main_Window(QMainWindow):

    # Run initial
    def __init__(self):
        super().__init__()
        self.initUI()

    # Button initial
    def initBTN(self):
        btn_quit = QPushButton('Quit', self)
        btn_quit.move(420, 620)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.clicked.connect(QCoreApplication.instance().quit)

        btn_loadfile = QPushButton('Load', self)
        btn_loadfile.move(50, 50)
        btn_loadfile.clicked.connect(self.initLOAD)

    # FileLoad def
    def initLOAD(self):
        fname = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
        print(fname[0])
        print(fname[1])

    # StatusBar initial
    def initSTATUS(self):
        self.statusBar().showMessage('Ready')

    # MenuBar initial
    def initMENU(self):
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QCoreApplication.instance().quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

    # MainUI initial
    def initUI(self):
        self.setWindowTitle('YANA')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(300, 300, 515, 660)
        self.setFixedSize(515, 660)
        Main_Window.initBTN(self)
        Main_Window.initSTATUS(self)
        Main_Window.initMENU(self)

        #self.move(300, 300)
        #self.resize(515,659)
        self.show()
