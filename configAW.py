from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Authentification(object):
    def setupUi(self, Authentification):
        if not Authentification.objectName():
            Authentification.setObjectName(u"Authentification")
        Authentification.setEnabled(True)
        Authentification.resize(515, 470)
        Authentification.setStyleSheet(u"background-color:rgb(255, 192, 64)")
        self.centralwidget = QWidget(Authentification)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 260, 201, 31))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color:rgb(255, 64, 17)")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 20, 91, 31))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(24)
        self.label.setFont(font1)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(23, 70, 441, 41))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(18)
        self.plainTextEdit.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 110, 101, 51))
        self.label_2.setFont(font1)
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(33, 170, 431, 41))
        self.plainTextEdit_2.setFont(font2)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 320, 221, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color:rgb(255, 64, 17)")
        self.statusbar = QStatusBar(Authentification)
        self.statusbar.setObjectName(u"statusbar")

        self.retranslateUi(Authentification)

        QMetaObject.connectSlotsByName(Authentification)
    # setupUi

    def retranslateUi(self, Authentification):
        Authentification.setWindowTitle(QCoreApplication.translate("Authentification", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Authentification", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("Authentification", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("Authentification", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Authentification", u"\u041f\u0440\u043e\u0439\u0442\u0438 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044e", None))
    # retranslateUi

