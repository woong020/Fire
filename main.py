# Source import
import ui
import FireUI

# Pakage import
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


# Main code
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    #WindowClass의 인스턴스 생성
    myWindow = ui.WindowClass()
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