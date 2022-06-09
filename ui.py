# import .py
import graph

# import package
import sys
import os.path
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar



# UI파일 연결
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path("FireUI.ui")
form_class = uic.loadUiType(form)[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    # Main initial
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()

    # AddUI initial
    def initUI(self):
        self.setWindowTitle('Lonely Death')
        icon_dir = resource_path("./.ico/icon.png")
        self.setWindowIcon(QIcon(icon_dir))
        self.initSTATUS()
        self.initMENU()
        self.initBTN()
        self.initLOGO()
        self.initPlotGraph()

    # Logo initial
    def initLOGO(self):
        logo_dir = resource_path("./.ico/logo.png")
        logo = QPixmap(logo_dir)
        logo_img = logo.scaled(QSize(100, 100), aspectRatioMode=Qt.KeepAspectRatio)
        self.label_LOGO.setPixmap(logo_img)

    # Button initial
    def initBTN(self):
        self.btn_LOADFILE.clicked.connect(lambda : self.initBtnFileLoad())
        self.btn_RESET.clicked.connect(lambda : self.initBtnFileReset())
        self.btn_RUN.clicked.connect(lambda : self.initBtnRun())
        # 실행 시 Heatmap radio button 클릭 상태
        self.radiobtn_HEATMAP.toggle()
        # 실행 시 추세선, contents combobox 비활성화
        self.checkBox_TREND.setEnabled(False)
        self.comboBoxCONTENTS.setEnabled(False)
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

        if self.labelgetFILE1.text() == '':
            self.labelgetFILE1.setText(fname[0])
            self.statusBar().showMessage('File1 Ready')

        elif self.labelgetFILE2.text() == '':
            self.labelgetFILE2.setText(fname[0])
            self.statusBar().showMessage('File2 Ready')

        elif self.labelgetFILE3.text() == '':
            self.labelgetFILE3.setText(fname[0])
            self.statusBar().showMessage('File3 Ready')

        elif self.labelgetFILE4.text() == '':
            self.labelgetFILE4.setText(fname[0])
            self.statusBar().showMessage('File4 Ready')
        else:
            QMessageBox.information(self, "Error", "All files are ready")

    # Select File Reset
    def initBtnFileReset(self):
        select = "Select"

        self.labelgetFILE1.setText('')
        self.labelgetFILE2.setText('')
        self.labelgetFILE3.setText('')
        self.labelgetFILE4.setText('')
        self.fig.clear()
        self.canvas.draw()
        self.radiobtn_HEATMAP.toggle()
        self.comboBoxAREA.setCurrentText(select)
        self.comboBoxCONTENTS.setCurrentText(select)
        self.checkBox_TREND.setEnabled(False)
        self.comboBoxCONTENTS.setEnabled(False)
        self.statusBar().showMessage('Reset All')

    # Select Radio 1
    def initRadBtnHeatmap(self):
        self.checkBox_TREND.setEnabled(False)
        self.comboBoxCONTENTS.setEnabled(False)
        self.statusBar().showMessage('select Heatmap')

    # Select Radio 2
    def initRadBtnGraph(self):
        self.checkBox_TREND.setEnabled(True)
        self.checkBox_TREND.toggle()
        self.comboBoxCONTENTS.setEnabled(True)
        self.statusBar().showMessage('select Graph')

    # initial Graph ToolBar
    def initToolBar(canvas, self):
        toolbar = NavigationToolbar(canvas, self.widget_GRAPH)
        return toolbar

    # initial Graph
    def initPlotGraph(self):
        self.fig = plt.Figure()
        # plt, sns 한글 폰트 옵션
        plt.rc("font", family="Malgun Gothic")
        sns.set(font="Malgun Gothic",
                rc={"figure.figsize":(5, 5), "axes.unicode_minus": False}, style='darkgrid')

        # canvas 생성
        self.canvas = FigureCanvas(self.fig)
        toolbar = WindowClass.initToolBar(self.canvas, self)
        self.canvas.draw()

        # toolbar, canvas 정렬
        self.verticalLayout_plot.addWidget(toolbar)
        self.verticalLayout_plot.addWidget(self.canvas)

    # Run Button initial
    def initBtnRun(self):
        if self.labelgetFILE4.text() == '':
            QMessageBox.information(self, "Error", "Please File load")
        else:
            combo_area = self.comboBoxAREA.currentText()
            if combo_area == 'Select':
                QMessageBox.information(self, "Error", "Please Select Area")

            else:
                areacode = WindowClass.initComboArea(combo_area)

                # file path 전달 및 csv read
                data1, data2, data3, data4 = graph.setDataCsv(self.labelgetFILE1.text(), self.labelgetFILE2.text(),
                                                              self.labelgetFILE3.text(), self.labelgetFILE4.text())
                # read 된 csv dataframe화
                df_local, df_local_corr, opt, df_local2, df_local3, df_local4 = \
                    graph.setFrame2Inf(data1, data2, data3, data4)

                # fig(plt.Figure) 초기화 및 subplot 생성
                self.fig.clear()
                ax = self.fig.add_subplot(111)

                # Heatmap 그래프 생성
                if self.radiobtn_HEATMAP.isChecked():
                    graph.setInf2Heat(df_local_corr, areacode, ax)
                    self.fig.tight_layout()
                    self.canvas.draw()
                    self.statusBar().showMessage('Executed Heatmap')
                    corr = graph.initCorrHeatmap(df_local_corr, areacode)
                    self.labelgetCORR.setText(corr)

                # regplot 생성
                else:
                    contentsname = self.comboBoxCONTENTS.currentText()
                    if contentsname == 'Select':
                        QMessageBox.information(self, "Error", "Please Select Contents")

                    # 추세선 옵션에 따른 if문
                    else:
                        contentscode = WindowClass.initComboContents(contentsname)
                        if self.checkBox_TREND.isChecked():
                            corr = graph.initReg.setInf2Reg(df_local, areacode, contentscode, opt, ax,
                                                     df_local2, df_local3, df_local4)
                            self.labelgetCORR.setText(corr)
                        else:
                            corr = graph.initReg.setInf2RegisnotCheck(df_local, areacode, contentscode, opt, ax,
                                                               df_local2, df_local3, df_local4)
                            self.labelgetCORR.setText(corr)
                        self.fig.tight_layout()
                        self.canvas.draw()
                        self.statusBar().showMessage('Executed Regplot')


    # Combobox Area to AreaCode
    def initComboArea(self):
        areaname = self
        if areaname == '전국':
            areacode = 0
        elif areaname == '서울':
            areacode = 1
        elif areaname == '강원':
            areacode = 2
        elif areaname == '경기':
            areacode = 3
        elif areaname == '경남':
            areacode = 4
        elif areaname == '경북':
            areacode = 5
        elif areaname == '광주':
            areacode = 6
        elif areaname == '대구':
            areacode = 7
        elif areaname == '대전':
            areacode = 8
        elif areaname == '부산':
            areacode = 9
        elif areaname == '세종':
            areacode = 10
        elif areaname == '울산':
            areacode = 11
        elif areaname == '인천':
            areacode = 12
        elif areaname == '전북':
            areacode = 13
        elif areaname == '전남':
            areacode = 14
        elif areaname == '제주':
            areacode = 15
        elif areaname == '충북':
            areacode = 16
        elif areaname == '충남':
            areacode = 17
        else:
            QMessageBox.information(self, "Error", "Please Select Area")
        return areacode

    def initComboContents(self):
        contentsname = self
        if contentsname == '기초생활수급자':
            contentscode = 1
        elif contentsname == '1인가구':
            contentscode = 2
        elif contentsname == '실업자':
            contentscode = 3

        return contentscode

    # Close Event
    def closeEvent(self, event,):
        reply = QMessageBox.question(self, 'EXIT', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
