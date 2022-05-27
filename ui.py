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
        self.radiobtn_CURVED.clicked.connect(lambda  : self.initRadBtnCurved())
        self.radiobtn_DISTRIBUTED.clicked.connect(lambda: self.initRadBtnDistributed())

    # StatusBar initial
    def initSTATUS(self):
        self.statusBar().showMessage('Ready')

    # MenuBar initial
    def initMENU(self):
        # Menu Action initial
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QCoreApplication.instance().quit)

        abouttext = "This program is a hands-on program for data analysis in the first semester of 2022 and was produced by Team Fire.\n" \
                    "It cannot be copied or used without permission and requires the consent of the manufacturer.\n\n " \
                    "Powerd by 오픈 소스 소프트웨어 기반\n" \
                    " Copyright ⓒ 2022 Team Fire"
        aboutAction = QAction('About', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.triggered.connect(lambda : QMessageBox.about(self, 'About', abouttext))


        # Menu bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        helpmenu = menubar.addMenu('&Help')
        helpmenu.addAction(aboutAction)

    # 파일 선택 1
    def initBtnFileLoad1(self):
        global fname1
        fname1 = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
        self.labelgetFILE1.setText(fname1[0])
        self.statusBar().showMessage('File1 Ready')

    # 파일 선택 2
    def initBtnFileLoad2(self):
        global fname2
        fname2 = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
        self.labelgetFILE2.setText(fname2[0])
        self.statusBar().showMessage('File2 Ready')

    # 꺾은선 선택
    def initRadBtnCurved(self):
        global lineopt
        lineopt = 0
        print(lineopt)

    # 분산형 선택
    def initRadBtnDistributed(self):
        global lineopt
        lineopt = 1
        print(lineopt)
