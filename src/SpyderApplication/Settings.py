# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import serial.tools.list_ports
import Application3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(433, 340)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 81, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Unselect")
        self.comboBox.setCurrentIndex(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.BaudRateSlider = QtWidgets.QSlider(self.centralwidget)
        self.BaudRateSlider.setGeometry(QtCore.QRect(20, 140, 19, 141))
        self.BaudRateSlider.setMaximum(4)
        self.BaudRateSlider.setPageStep(4)
        self.BaudRateSlider.setProperty("value", 4)
        self.BaudRateSlider.setSliderPosition(1)
        self.BaudRateSlider.setOrientation(QtCore.Qt.Vertical)
        self.BaudRateSlider.setObjectName("BaudRateSlider")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 237, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 203, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 140, 51, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 268, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 91, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 0, 16, 301))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        SettingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SettingsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 24))
        self.menubar.setObjectName("menubar")
        SettingsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SettingsWindow)
        self.statusbar.setObjectName("statusbar")
        SettingsWindow.setStatusBar(self.statusbar)
        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "MainWindow"))
        self.label.setText(_translate("SettingsWindow", "COM PORT"))
        self.label_2.setText(_translate("SettingsWindow", "9600"))
        self.label_3.setText(_translate("SettingsWindow", "14400"))
        self.label_4.setText(_translate("SettingsWindow", "19200"))
        self.label_5.setText(_translate("SettingsWindow", "115200"))
        self.label_6.setText(_translate("SettingsWindow", "4800"))
        self.label_7.setText(_translate("SettingsWindow", "BAUD RATE"))
        
    def SearchForAvailableCOMS(self):
    
        for p in serial.tools.list_ports.comports():
            self.comboBox.addItem(p.device)
            
            
            
    
    def GetBaudRate(self):
        if (self.BaudRateSlider.value() == 0):
            return 4800
        elif (self.BaudRateSlider.value() == 1):
            return 9600
        elif (self.BaudRateSlider.value() == 1):
            return 14400
        elif (self.BaudRateSlider.value() == 1):
            return 19200
        elif (self.BaudRateSlider.value() == 1):
            return 115200
        
    def GetComName(self):
      if (self.comboBox.currentIndex() == 0):
          return 0
      elif (self.comboBox.currentIndex() == 1):
          return 1
      else:
          return -1
        
    def ComSelection(self):
        self.ui = Application3.Ui_MainWindow()
        self.comboBox.currentIndexChanged.connect(self.ui.InitSerialCommunication)
    def BaudSelection(self):
        self.ui = Application3.Ui_MainWindow()
        self.BaudRateSlider.valueChanged.connect(self.ui.InitSerialCommunication)    
if __name__ == "__main__":
    import sys
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QMainWindow()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    ui.SearchForAvailableCOMS()
    SettingsWindow.show()
    app.exec_()

