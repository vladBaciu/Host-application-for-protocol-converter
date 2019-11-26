# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import Application3
from PyQt5 import QtCore, QtGui, QtWidgets
detectChanges = False
class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.setFixedSize(213, 360)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 181, 261))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 285, 101, 27))
        self.pushButton.setObjectName("pushButton")
        SettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 213, 24))
        self.menubar.setObjectName("menubar")
        SettingsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "SettingsWindow"))
        self.pushButton.setText(_translate("SettingsWindow", "Save settings"))

    def exitCall(self):
        print("Kill second window....")
        import sys
        sys.exit() 
        
    def ReadInitFile(self):
         with open('InitFile.ini','r') as commandsFile:
             content = commandsFile.read()
             self.textEdit.append(content)
             
    def WriteToFile(self):
         global detectChanges;
         detectChanges = True;
         with open('InitFile.ini','w') as commandsFile:
             content = self.textEdit.toPlainText()
             commandsFile.write(content)
#         self.exitCall()
             
    def CheckButton(self):
        self.pushButton.clicked.connect(self.WriteToFile)
      
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    app.exec_()

