import graph

import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

global fname1
fname1 = ''
global fname2
fname2 = ''

class Main_Window(QMainWindow):

    # Run initial
    def __init__(self):
        super().__init__()
        self.initUI()

        self.data1 = 0
        self.data2 = 0

    # Button initial
    def initBTN(self):
        btn_quit = QPushButton('Quit', self)
        btn_quit.move(360, 620)
        btn_quit.resize(btn_quit.sizeHint())
        btn_quit.clicked.connect(QCoreApplication.instance().quit)

        btn_first_loadfile = QPushButton('File 1', self)
        btn_first_loadfile.move(50, 50)
        btn_first_loadfile.clicked.connect(self.initLOAD1)

        btn_seccond_loadfile = QPushButton('File 2', self)
        btn_seccond_loadfile.move(200, 50)
        btn_seccond_loadfile.clicked.connect(self.initLOAD2)

    # FileLoad def
    def initLOAD1(self):
        fname = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
        print(fname[0])
        print(fname[1])

        graph.Main_graph.initDATA1(fname[0])

    # FileLoad def
    def initLOAD2(self):
        global fname
        fname = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
        print(fname[0])
        print(fname[1])

        #graph.Main_graph.initDATA2(fname[0])

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
        self.setGeometry(100, 100, 515, 700)
        self.setFixedSize(515, 700)
        Main_Window.initBTN(self)
        Main_Window.initSTATUS(self)
        Main_Window.initMENU(self)

        #self.move(300, 300)
        #self.resize(515,659)
        self.show()

