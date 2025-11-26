# -*- coding: utf-8 -*-
import sys
import os
from PySide6 import QtCore,QtGui,QtWidgets
from PUFE import Ui_MainWindow

selfDir = os.getcwd()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent) 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton1.clicked.connect(self.pushButton1_clicked)
        self.ui.pushButton2.clicked.connect(self.pushButton2_clicked)
        self.ui.pushButton3.clicked.connect(self.pushButton3_clicked)
        self.ui.pushButton4.clicked.connect(self.pushButton4_clicked)
        self.ui.pushButton5.clicked.connect(self.pushButton5_clicked)

        if os.path.isfile(selfDir + "/setting.txt") == True:
            text = ""
            f = open(selfDir + "/setting.txt", "r")
            text = f.readlines()
            f.close()
            self.ui.lineEdit1.setText(text[0].replace("\n", ""))
            self.ui.lineEdit2.setText(text[1].replace("\n", ""))

    def saveData(self):
        text = self.ui.lineEdit1.text() + "\n" + self.ui.lineEdit2.text() + "\n"
        f = open(selfDir + "/setting.txt", "w")
        f.writelines(text)
        f.close()

    def pushButton1_clicked(self):
        self.ui.lineEdit1.setText("")
        self.saveData()

    def pushButton2_clicked(self):
        FilePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "bat and exe File", "",'bat and exe File (*.bat *.exe)')
        if FilePath:
            self.ui.lineEdit1.setText(FilePath)
            self.saveData()

    def pushButton3_clicked(self):
        self.ui.lineEdit2.setText("")
        self.saveData()

    def pushButton4_clicked(self):
        if os.path.isfile(self.ui.lineEdit1.text()) == False:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("Message")
            msgbox.setText("Please set the path to Pyside6-uic.")
            ret = msgbox.exec_()
        elif os.path.isfile(self.ui.lineEdit2.text()) == False:
            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("Message")
            msgbox.setText("Please select a python file.")
            ret = msgbox.exec_()
        else:
            puPath = self.ui.lineEdit1.text() + " "
            uiPath = self.ui.lineEdit2.text() + " -o "
            filename1 = uiPath.rsplit(".", 1)
            filename2 = filename1[0].rsplit("/", 1)
            pyPath = filename1[0] + ".py"
            os.chdir(filename2[0] + "/")

            cmd = puPath + uiPath + pyPath

            msgbox = QtWidgets.QMessageBox(self)
            msgbox.setWindowTitle("Message")
            msgbox.setText(cmd)
            ret = msgbox.exec_()

            ret = os.system(cmd)
            if ret == 0:
                msgbox = QtWidgets.QMessageBox(self)
                msgbox.setWindowTitle("Message")
                msgbox.setText("The selected file is converted.")
                ret = msgbox.exec_()
            else: 
                msgbox = QtWidgets.QMessageBox(self)
                msgbox.setWindowTitle("Message")
                msgbox.setText("ERROR CODE : " + str(ret))
                ret = msgbox.exec_()

    def pushButton5_clicked(self):
        FilePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "ui File", "",'ui File (*.ui)')
        if FilePath:
            self.ui.lineEdit2.setText(FilePath)
            self.saveData()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dlg = MainWindow()
    dlg.show()
    sys.exit(app.exec_())
