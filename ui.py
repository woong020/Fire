# import .py

# import package
import sys
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, QSize, Qt
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQT as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure




# UI파일 연결
form_class = uic.loadUiType("FireUI.ui")[0]

class About(QWidget):
    def initUI(self):
        self.setWindowTitle('Fire')
        self.setWindowIcon(QIcon('.ico\\Fire.png'))
        self.show()


global filecnt
filecnt = 0
global lineopt
lineopt = 0

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
        # self.initCheckTrend()
        self.initLOGO()

    # Logo initial
    def initLOGO(self):
        # logo.png locate find
        path_dir = os.getcwd()
        logo_dir = path_dir + "\\.ico\\logo.png"
        logo = QPixmap(logo_dir)
        logo_img = logo.scaled(QSize(100, 100), aspectRatioMode=Qt.KeepAspectRatio)
        self.label_LOGO.setPixmap(logo_img)

    # Button initial
    def initBTN(self):
        self.btnLOADFILE.clicked.connect(lambda : self.initBtnFileLoad())
        self.btnRESET.clicked.connect(lambda : self.initBtnFileReset())
        self.radiobtn_HEATMAP.toggle()
        self.checkBox_TREND.setEnabled(False)
        self.radiobtn_HEATMAP.clicked.connect(lambda  : self.initRadBtnHeatmap())
        self.radiobtn_GRAPH.clicked.connect(lambda: self.initRadBtnGraph())

    # StatusBar initial
    def initSTATUS(self):
        self.statusBar().showMessage('Ready')

    # MenuBar initial
    def initMENU(self):
        # Menu Action initial
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(lambda : self.close())
        # exitAction.triggered.connect(QCoreApplication.instance().quit)

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

    # Select File
    def initBtnFileLoad(self):
        fname = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
        global filecnt

        if filecnt == 0:
            self.labelgetFILE1.setText(fname[0])
            self.statusBar().showMessage('File1 Ready')
            filecnt += 1

        elif filecnt == 1:
            self.labelgetFILE2.setText(fname[0])
            self.statusBar().showMessage('File2 Ready')
            filecnt += 1

        elif filecnt == 2:
            self.labelgetFILE3.setText(fname[0])
            self.statusBar().showMessage('File3 Ready')
            filecnt += 1

        elif filecnt == 3:
            self.labelgetFILE4.setText(fname[0])
            self.statusBar().showMessage('File4 Ready')
            filecnt += 1
        else:
            QMessageBox.information(self, "Error", "Already all file")


    # Select File Reset
    def initBtnFileReset(self):
        global filecnt
        filecnt = 0

        self.labelgetFILE1.setText(' ')
        self.labelgetFILE2.setText(' ')
        self.labelgetFILE3.setText(' ')
        self.labelgetFILE4.setText(' ')


    # Select Radio 1
    def initRadBtnHeatmap(self):
        global lineopt
        lineopt = 0
        self.checkBox_TREND.setEnabled(False)


    # Select Radio 2
    def initRadBtnGraph(self):
        global lineopt
        lineopt = 1
        self.checkBox_TREND.setEnabled(True)

    def initPlotGraph(self):
        fig = plt.Figure()
        canvas = FigureCanvas(fig)



    # Close Event
    def closeEvent(self, event,):
        reply = QMessageBox.question(self, 'EXIT', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
