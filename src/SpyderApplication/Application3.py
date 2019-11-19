# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Application.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


FBL_GET_VERSION_CMD = "0x14"
FBL_GET_HELP_CMD = "0x22"
FBL_GET_CID_CMD = "0x44"
FBL_GET_RDP_LEVEL_CMD = "0x25"
FBL_GO_TO_ADDR_CMD = "0x19"
FBL_ERASE_FLASH_CMD = "0x84"
FBL_MEMORY_WRITE_CMD = "0x32"
FBL_ENABLE_RW_PROTECTION_CMD = "0x3C"
FBL_MEMORY_READ_CMD = "0x2B"
FBL_READ_SECTOR_PROTECTION_STATUS_CMD = "0x78"
FBL_READ_OTP_CMD = "0x1F"
FBL_DISABLE_RW_PROTECTION_CMD = "0x6C"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(567, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 80, 541, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.USB = QtWidgets.QWidget()
        self.USB.setObjectName("USB")
        self.label_2 = QtWidgets.QLabel(self.USB)
        self.label_2.setGeometry(QtCore.QRect(350, 0, 241, 191))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.USB)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 131, 31))
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.USB)
        self.pushButton.setGeometry(QtCore.QRect(260, 90, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.USB)
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 241, 261))
        self.listWidget.setObjectName("listWidget")
        self.comboBox_3 = QtWidgets.QComboBox(self.USB)
        self.comboBox_3.setGeometry(QtCore.QRect(160, 20, 131, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.USB)
        self.textBrowser.setGeometry(QtCore.QRect(260, 210, 271, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.USB)
        self.textBrowser_2.setGeometry(QtCore.QRect(260, 290, 271, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_5 = QtWidgets.QLabel(self.USB)
        self.label_5.setGeometry(QtCore.QRect(260, 190, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.USB)
        self.label_6.setGeometry(QtCore.QRect(260, 270, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.USB, "")
        self.WiFi = QtWidgets.QWidget()
        self.WiFi.setObjectName("WiFi")
        self.label_3 = QtWidgets.QLabel(self.WiFi)
        self.label_3.setGeometry(QtCore.QRect(250, -20, 201, 171))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.WiFi)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.WiFi)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 280, 111, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_4 = QtWidgets.QComboBox(self.WiFi)
        self.comboBox_4.setGeometry(QtCore.QRect(120, 30, 131, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.listWidget_2 = QtWidgets.QListWidget(self.WiFi)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 90, 131, 251))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.tabWidget.addTab(self.WiFi, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(280, -60, 281, 131))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, -60, 201, 121))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/modes/dependences/UsbModeLogo.png\"/><img src=\":/modes/UsbModeLogo.png\"/></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Loader Mode"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Application mode"))
        self.pushButton.setText(_translate("MainWindow", "SEND COMMAND"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "USB to UART"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "USB to CAN"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "USB to WI-FI"))
        self.label_5.setText(_translate("MainWindow", "Transmit status"))
        self.label_6.setText(_translate("MainWindow", "Receive status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.USB), _translate("MainWindow", "USB"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/modes/dependences/WifiModelLogo.png\"/></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Loader Mode"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Application mode"))
        self.pushButton_2.setText(_translate("MainWindow", "SEND COMMAND"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "USB to UART"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "USB to CAN"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "USB to WI-FI"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Get version 0x51"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WiFi), _translate("MainWindow", "WiFi"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Logo/dependences/9741ef35-9950-4396-9d31-0876fc97d6a3_200x200.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/modes/dependences/MyNameLogo.png\"/></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        
    def ReadCommands(self, MainWindow):
        self.listWidget.setStyleSheet("font: 8pt Comic Sans MS")
        with open('SupportedCommands.txt','r') as commandsFile:
            for commands in commandsFile:
                self.listWidget.addItem(commands)
                      
    def SendCommand(self, MainWindow):
        items = self.listWidget.selectedItems()
        self.textBrowser.clear()
        self.textBrowser.append(self.listWidget.currentItem().text())
        word_list = self.listWidget.currentItem().text().split()
        
        if (FBL_GET_VERSION_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_GET_HELP_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_GET_CID_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_GET_RDP_LEVEL_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_GO_TO_ADDR_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_ERASE_FLASH_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_MEMORY_WRITE_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_ENABLE_RW_PROTECTION_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_MEMORY_READ_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_READ_SECTOR_PROTECTION_STATUS_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_READ_OTP_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
        elif (FBL_DISABLE_RW_PROTECTION_CMD == word_list[-1]):
            self.textBrowser.append(word_list[-1])
            
                
    def CheckButton(self, MainWindow):
        self.pushButton.clicked.connect(self.SendCommand)



import LogoLabel_rc
import Usb_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.ReadCommands(MainWindow)
    ui.CheckButton(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

