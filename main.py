import sys
from PySide2 import QtCore, QtGui, QtWidgets
from configAW import Ui_Authentification
from configRW import Ui_Registration

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Authentification()
ui.setupUi(Dialog)
Dialog.show()

def OpenRegistForm():
    global Dialog
    Dialog = QtWidgets.QDialog()
    ui = Ui_Registration()
    ui.setupUi(Dialog)
    Dialog.show()

ui.pushButton_2.clicked.connect(OpenRegistForm)

sys.exit(app.exec_())