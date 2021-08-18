from PyQt5 import QtWidgets
import sys 

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()

window.resize(500,500)
window.move(100,100)
window.show()