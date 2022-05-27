import matplotlib.pyplot as plt
#import graph

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets, uic
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.backends.backend_qt5agg import FigureCanvasQT as FigureCanvas
# from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure

# UI파일 연결
form_class = uic.loadUiType("FireUI.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()

    # AddUI initial
    def initUI(self):
        self.setWindowTitle('Fire')
        self.setWindowIcon(QIcon('icon.png'))
        self.initSTATUS()
        self.initMENU()
        self.initBTN()

    # Button initial
    def initBTN(self):

        self.btnLOADFILE1.clicked.connect(lambda : self.initBtnFileLoad1())
        self.btnLOADFILE2.clicked.connect(lambda : self.initBtnFileLoad2())

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

    # 파일 선택 1
    def initBtnFileLoad1(self):
        global fname1
        fname1 = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
        self.labelgetFILE1.setText(fname1[0])

    # 파일 선택 2
    def initBtnFileLoad2(self):
        global fname2
        fname2 = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
        self.labelgetFILE2.setText(fname2[0])
