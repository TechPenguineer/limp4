import sys
from PyQt5 import QtCore, QtWidgets


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("LIMP4")

        openAction = QtWidgets.QAction("&Open", self)
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip('Open a file')

        extractAction = QtWidgets.QAction("&Quit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')

        extractAction.triggered.connect(self.close_application)
        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')

        fileMenu.addAction(openAction)
        fileMenu.addAction(extractAction)
        
        self.home()

    def home(self):
        self.show()

    def close_application(self):
        print("whooaaaa so custom!!!")
        sys.exit()


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()