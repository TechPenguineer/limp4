from PyQt5 import QtWidgets
import sys 
import yaml



app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()

window.resize(500,500)
window.move(100,100)
window.show()
window.setWindowTitle("Limp4")

sys.exit(app.exec_())