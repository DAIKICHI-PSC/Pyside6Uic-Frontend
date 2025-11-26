# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PUFE.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 152)
        MainWindow.setMinimumSize(QSize(1051, 152))
        MainWindow.setMaximumSize(QSize(1051, 152))
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox1 = QGroupBox(self.centralwidget)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setGeometry(QRect(10, 10, 1031, 61))
        font = QFont()
        font.setPointSize(9)
        self.groupBox1.setFont(font)
        self.lineEdit1 = QLineEdit(self.groupBox1)
        self.lineEdit1.setObjectName(u"lineEdit1")
        self.lineEdit1.setGeometry(QRect(10, 20, 811, 31))
        self.lineEdit1.setFont(font)
        self.pushButton2 = QPushButton(self.groupBox1)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setGeometry(QRect(930, 20, 93, 31))
        self.pushButton2.setFont(font)
        self.pushButton1 = QPushButton(self.groupBox1)
        self.pushButton1.setObjectName(u"pushButton1")
        self.pushButton1.setGeometry(QRect(830, 20, 93, 31))
        self.pushButton1.setFont(font)
        self.groupBox2 = QGroupBox(self.centralwidget)
        self.groupBox2.setObjectName(u"groupBox2")
        self.groupBox2.setGeometry(QRect(10, 80, 1031, 61))
        self.groupBox2.setFont(font)
        self.lineEdit2 = QLineEdit(self.groupBox2)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setGeometry(QRect(10, 20, 711, 31))
        self.lineEdit2.setFont(font)
        self.pushButton5 = QPushButton(self.groupBox2)
        self.pushButton5.setObjectName(u"pushButton5")
        self.pushButton5.setGeometry(QRect(930, 20, 93, 31))
        self.pushButton5.setFont(font)
        self.pushButton4 = QPushButton(self.groupBox2)
        self.pushButton4.setObjectName(u"pushButton4")
        self.pushButton4.setGeometry(QRect(830, 20, 93, 31))
        self.pushButton4.setFont(font)
        self.pushButton3 = QPushButton(self.groupBox2)
        self.pushButton3.setObjectName(u"pushButton3")
        self.pushButton3.setGeometry(QRect(730, 20, 93, 31))
        self.pushButton3.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pyside6-uic Front End", None))
        self.groupBox1.setTitle(QCoreApplication.translate("MainWindow", u"LOCATION OF pyside6-uic.bat", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.pushButton1.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.groupBox2.setTitle(QCoreApplication.translate("MainWindow", u"LOCATION OF UI FILE", None))
        self.pushButton5.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.pushButton4.setText(QCoreApplication.translate("MainWindow", u"EXEC", None))
        self.pushButton3.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
    # retranslateUi

