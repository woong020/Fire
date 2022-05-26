# Source import
import graph


# Pakage import
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQT as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# UI파일 연결
form_class = uic.loadUiType("FireUI.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        # Ui 구성 추가
        self.setWindowTitle('Fire')
        self.setWindowIcon(QIcon('icon.png'))
        self.initSTATUS()
        self.initMENU()
        self.initBTN()

    def initBTN(self):
        # 버튼 기능 연결
        self.btnLOADFILE1.clicked.connect(self.initBtnFileLoad1())
        self.btnLOADFILE2.clicked.connect(self.initBtnFileLoad2())

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

    def initBtnFileLoad1(self):
        print("Load1")
        global fname1
        fname1 = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
        graph.Main_graph.initDATA1(fname1[0])

    def initBtnFileLoad2(self):
        print("Load2")
        # fname1 = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
        # #graph.Main_graph.initDATA2(fname1[0])



# class WindowClass(QMainWindow):
#     # Run initial
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#
#     # Button initial
#     # def initBTN(self):
#     #     # btn_quit = QPushButton('Quit', self)
#     #     # btn_quit.move(360, 620)
#     #     # btn_quit.resize(btn_quit.sizeHint())
#     #     # btn_quit.clicked.connect(QCoreApplication.instance().quit)
#     #
#     #     btn_first_loadfile = QPushButton('File 1', self)
#     #     btn_first_loadfile.move(50, 50)
#     #     btn_first_loadfile.clicked.connect(self.initLOAD1)
#     #
#     #     btn_seccond_loadfile = QPushButton('File 2', self)
#     #     btn_seccond_loadfile.move(200, 50)
#     #     btn_seccond_loadfile.clicked.connect(self.initLOAD2)
#     #
#     #     btn_plot_graph = QPushButton('Run', self)
#     #     btn_plot_graph.move(350, 50)
#
#     # FileLoad def
#     def initBTNFILELOAD1(self):
#         fname1 = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
#         print(fname1[0])
#         print(fname1[1])
#
#         # graph.Main_graph.initDATA1(fname1[0])
#
#     # FileLoad def
#     def initLOAD2(self):
#         global fname1
#         fname1 = QFileDialog.getOpenFileName(self, '', '', 'All File(*);; Exel Data(*.csv)')
#         print(fname1[0])
#         print(fname1[1])
#
#         # graph.Main_graph.initDATA2(fname1[0])
#
#     # StatusBar initial
#     def initSTATUS(self):
#         self.statusBar().showMessage('Ready')
#
#     # MenuBar initial
#     def initMENU(self):
#         exitAction = QAction('Exit', self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.triggered.connect(QCoreApplication.instance().quit)
#
#         menubar = self.menuBar()
#         menubar.setNativeMenuBar(False)
#         filemenu = menubar.addMenu('&File')
#         filemenu.addAction(exitAction)
#
#     # MainUI initial
#     def initUI(self):
#         Dialog = self
#         self.setWindowTitle('Fire')
#         self.setWindowIcon(QIcon('icon.png'))
#
#
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(483, 704)
#         Dialog.setMinimumSize(QtCore.QSize(0, 704))
#         self.groupBox_FILE = QtWidgets.QGroupBox(Dialog)
#         self.groupBox_FILE.setGeometry(QtCore.QRect(21, 160, 439, 91))
#         self.groupBox_FILE.setTitle("")
#         self.groupBox_FILE.setObjectName("groupBox_FILE")
#         self.widget = QtWidgets.QWidget(self.groupBox_FILE)
#         self.widget.setGeometry(QtCore.QRect(11, 11, 421, 71))
#         self.widget.setObjectName("widget")
#         self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
#         self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_4.setObjectName("verticalLayout_4")
#         self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_4.setObjectName("horizontalLayout_4")
#         self.label_FILE1 = QtWidgets.QLabel(self.widget)
#         self.label_FILE1.setObjectName("label_FILE1")
#         self.horizontalLayout_4.addWidget(self.label_FILE1)
#         self.tableWidget = QtWidgets.QTableWidget(self.widget)
#         self.tableWidget.setObjectName("tableWidget")
#         self.tableWidget.setColumnCount(0)
#         self.tableWidget.setRowCount(0)
#         self.horizontalLayout_4.addWidget(self.tableWidget)
#         self.verticalLayout_4.addLayout(self.horizontalLayout_4)
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.label_FILE2 = QtWidgets.QLabel(self.widget)
#         self.label_FILE2.setObjectName("label_FILE2")
#         self.horizontalLayout_2.addWidget(self.label_FILE2)
#         self.tableWidget_2 = QtWidgets.QTableWidget(self.widget)
#         self.tableWidget_2.setObjectName("tableWidget_2")
#         self.tableWidget_2.setColumnCount(0)
#         self.tableWidget_2.setRowCount(0)
#         self.horizontalLayout_2.addWidget(self.tableWidget_2)
#         self.verticalLayout_4.addLayout(self.horizontalLayout_2)
#         self.groupBox_GRAPH = QtWidgets.QGroupBox(Dialog)
#         self.groupBox_GRAPH.setGeometry(QtCore.QRect(20, 320, 441, 371))
#         self.groupBox_GRAPH.setTitle("")
#         self.groupBox_GRAPH.setObjectName("groupBox_GRAPH")
#         self.widget_GRAPH = QtWidgets.QWidget(self.groupBox_GRAPH)
#         self.widget_GRAPH.setGeometry(QtCore.QRect(10, 20, 421, 341))
#         self.widget_GRAPH.setObjectName("widget_GRAPH")
#         self.groupBox_COR = QtWidgets.QGroupBox(Dialog)
#         self.groupBox_COR.setGeometry(QtCore.QRect(20, 260, 441, 51))
#         self.groupBox_COR.setTitle("")
#         self.groupBox_COR.setObjectName("groupBox_COR")
#         self.widget1 = QtWidgets.QWidget(self.groupBox_COR)
#         self.widget1.setGeometry(QtCore.QRect(10, 10, 421, 31))
#         self.widget1.setObjectName("widget1")
#         self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget1)
#         self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_6.setObjectName("horizontalLayout_6")
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.label_COE = QtWidgets.QLabel(self.widget1)
#         self.label_COE.setObjectName("label_COE")
#         self.horizontalLayout_3.addWidget(self.label_COE)
#         self.tableWidget_3 = QtWidgets.QTableWidget(self.widget1)
#         self.tableWidget_3.setObjectName("tableWidget_3")
#         self.tableWidget_3.setColumnCount(0)
#         self.tableWidget_3.setRowCount(0)
#         self.horizontalLayout_3.addWidget(self.tableWidget_3)
#         self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
#         self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
#         self.horizontalLayout_5.setObjectName("horizontalLayout_5")
#         self.label_REL = QtWidgets.QLabel(self.widget1)
#         self.label_REL.setObjectName("label_REL")
#         self.horizontalLayout_5.addWidget(self.label_REL)
#         self.tableWidget_4 = QtWidgets.QTableWidget(self.widget1)
#         self.tableWidget_4.setObjectName("tableWidget_4")
#         self.tableWidget_4.setColumnCount(0)
#         self.tableWidget_4.setRowCount(0)
#         self.horizontalLayout_5.addWidget(self.tableWidget_4)
#         self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
#         self.layoutWidget = QtWidgets.QWidget(Dialog)
#         self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 441, 141))
#         self.layoutWidget.setObjectName("layoutWidget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
#         self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.groupBox_SEL_FILE = QtWidgets.QGroupBox(self.layoutWidget)
#         self.groupBox_SEL_FILE.setTitle("")
#         self.groupBox_SEL_FILE.setObjectName("groupBox_SEL_FILE")
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_SEL_FILE)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout()
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.btnLOADFILE1 = QtWidgets.QPushButton(self.groupBox_SEL_FILE)
#         self.btnLOADFILE1.setObjectName("btnLOADFILE1")
#         ##구현 추가
#         self.btnLOADFILE1.clicked.connect(self.initBTNFILELOAD1())
#         self.verticalLayout_2.addWidget(self.btnLOADFILE1)
#         self.btnLOADFILE2 = QtWidgets.QPushButton(self.groupBox_SEL_FILE)
#         self.btnLOADFILE2.setObjectName("btnLOADFILE2")
#         self.verticalLayout_2.addWidget(self.btnLOADFILE2)
#         self.comboBoxAREA = QtWidgets.QComboBox(self.groupBox_SEL_FILE)
#         self.comboBoxAREA.setObjectName("comboBoxAREA")
#         self.comboBoxAREA.addItem("")
#         self.verticalLayout_2.addWidget(self.comboBoxAREA)
#         self.verticalLayout_3.addLayout(self.verticalLayout_2)
#         self.horizontalLayout.addWidget(self.groupBox_SEL_FILE)
#         self.groupBox_OPT = QtWidgets.QGroupBox(self.layoutWidget)
#         self.groupBox_OPT.setTitle("")
#         self.groupBox_OPT.setObjectName("groupBox_OPT")
#         self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_OPT)
#         self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 81, 111))
#         self.layoutWidget1.setObjectName("layoutWidget1")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
#         self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.radioButton_CURVED = QtWidgets.QRadioButton(self.layoutWidget1)
#         self.radioButton_CURVED.setObjectName("radioButton_CURVED")
#         self.verticalLayout.addWidget(self.radioButton_CURVED)
#         self.radioButton_DISTRIBUTED = QtWidgets.QRadioButton(self.layoutWidget1)
#         self.radioButton_DISTRIBUTED.setObjectName("radioButton_DISTRIBUTED")
#         self.verticalLayout.addWidget(self.radioButton_DISTRIBUTED)
#         self.checkBox_TREND = QtWidgets.QCheckBox(self.layoutWidget1)
#         self.checkBox_TREND.setObjectName("checkBox_TREND")
#         self.verticalLayout.addWidget(self.checkBox_TREND)
#         self.horizontalLayout.addWidget(self.groupBox_OPT)
#         self.groupBox_RUN = QtWidgets.QGroupBox(self.layoutWidget)
#         self.groupBox_RUN.setTitle("")
#         self.groupBox_RUN.setObjectName("groupBox_RUN")
#         self.btn_RUN = QtWidgets.QPushButton(self.groupBox_RUN)
#         self.btn_RUN.setGeometry(QtCore.QRect(-2, -10, 111, 161))
#         self.btn_RUN.setObjectName("btn_RUN")
#         self.horizontalLayout.addWidget(self.groupBox_RUN)
#         self.groupBox_LOGO = QtWidgets.QGroupBox(self.layoutWidget)
#         self.groupBox_LOGO.setTitle("")
#         self.groupBox_LOGO.setObjectName("groupBox_LOGO")
#         self.label_LOGO = QtWidgets.QLabel(self.groupBox_LOGO)
#         self.label_LOGO.setGeometry(QtCore.QRect(0, 10, 91, 121))
#         self.label_LOGO.setObjectName("label_LOGO")
#         self.horizontalLayout.addWidget(self.groupBox_LOGO)
#
#         self.retranslateUi(Dialog)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#         Dialog.setTabOrder(self.btnLOADFILE1, self.btnLOADFILE2)
#         Dialog.setTabOrder(self.btnLOADFILE2, self.comboBoxAREA)
#         Dialog.setTabOrder(self.comboBoxAREA, self.radioButton_CURVED)
#         Dialog.setTabOrder(self.radioButton_CURVED, self.radioButton_DISTRIBUTED)
#         Dialog.setTabOrder(self.radioButton_DISTRIBUTED, self.checkBox_TREND)
#         Dialog.setTabOrder(self.checkBox_TREND, self.btn_RUN)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
#         self.label_FILE1.setText(_translate("Dialog", "파일1:"))
#         self.label_FILE2.setText(_translate("Dialog", "파일2:"))
#         self.label_COE.setText(_translate("Dialog", "상관계수"))
#         self.label_REL.setText(_translate("Dialog", "상관관계"))
#         self.btnLOADFILE1.setText(_translate("Dialog", "첫번째 파일"))
#         self.btnLOADFILE2.setText(_translate("Dialog", "두번째 파일"))
#         self.comboBoxAREA.setItemText(0, _translate("Dialog", "지역선택"))
#         self.radioButton_CURVED.setText(_translate("Dialog", "꺾은선"))
#         self.radioButton_DISTRIBUTED.setText(_translate("Dialog", "분산형"))
#         self.checkBox_TREND.setText(_translate("Dialog", "추세선"))
#         self.btn_RUN.setText(_translate("Dialog", "분석 실행"))
#         self.label_LOGO.setText(_translate("Dialog", "TextLabel"))
#         # self.setWindowTitle('Fire')
#         # self.setWindowIcon(QIcon('icon.png'))
#         # self.setGeometry(100, 100, 515, 700)
#         # self.setFixedSize(515, 700)
#         #
#         # # show button
#         # Main_Window.initBTN(self)
#         # Main_Window.initSTATUS(self)
#         # Main_Window.initMENU(self)
#         #
#         # #show widget
#         # self.main_widget = QWidget()
#         # self.setCentralWidget(self.main_widget)
#         #
#         # canvas = FigureCanvas(Figure(figsize=(1, 1)))
#         # vbox = QVBoxLayout(self.main_widget)
#         # vbox.addWidget(canvas)
#         #
#         # self.addToolBar(NavigationToolbar(canvas, self))
#         #
#         # self.ax = canvas.figure.subplots()
#         # self.ax.plot([0, 1, 2], [1, 5, 3], '-')
#         #
#         # self.fig = plt.Figure()
#         # self.canvas = FigureCanvas(self.fig)
#         #
#         # #self.move(300, 300)
#         # #self.resize(515,659)
#         # self.show()
#


# Main code
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

# if __name__ == "__main__" :
#     #QApplication : 프로그램을 실행시켜주는 클래스
#     app = QApplication(sys.argv)
#     #WindowClass의 인스턴스 생성
#     mainWindow = QMainWindow()
#     #프로그램 화면을 보여주는 코드
#     mywindow = FireUI.Ui_Dialog()
#     mywindow.setupUi(mainWindow)
#     mainWindow.show()
#     #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
#     app.exec_()