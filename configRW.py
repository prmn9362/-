from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Registration(object):
    def setupUi(self, Registration):
        if not Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(515, 470)
        Registration.setStyleSheet(u"background-color:rgb(255, 192, 64)")
        self.centralwidget = QWidget(Registration)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 340, 201, 41))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color:rgb(255, 64, 17)")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 10, 231, 51))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(43, 70, 431, 41))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(18)
        self.plainTextEdit.setFont(font2)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 120, 241, 51))
        self.label_2.setFont(font1)
        self.plainTextEdit_2 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(43, 170, 431, 41))
        self.plainTextEdit_2.setFont(font2)
        self.plainTextEdit_3 = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(40, 260, 431, 41))
        self.plainTextEdit_3.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 220, 291, 31))
        self.label_3.setFont(font1)
        self.statusbar = QStatusBar(Registration)
        self.statusbar.setObjectName(u"statusbar")

        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Registration", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.label.setText(QCoreApplication.translate("Registration", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0432\u043e\u0439 \u043b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("Registration", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0432\u043e\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Registration", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c \u0435\u0449\u0435 \u0440\u0430\u0437", None))
    # retranslateUi

