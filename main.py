# Source import
import ui

# Pakage import
import sys
from PyQt5.QtWidgets import QApplication #, QMainWindow, QWidget, QPushButton, QAction, qApp
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import QCoreApplication

# Main code
if __name__ == '__main__':
    window = QApplication(sys.argv)
    ex = ui.Main_Window()
    sys.exit(window.exec_())