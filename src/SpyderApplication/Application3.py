# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Application.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import serial
import struct
import os
saveHandler = False
init_done = False
stillConnected = False
serialCOM = "";
baudRate = "";
serialComHandler = serial.Serial()
import Settings
from PyQt5 import QtCore, QtGui, QtWidgets


FBL_GET_VERSION_CMD = "0x14"
FBL_INTERNAL_GET_VERSION_CMD = 1
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
        self.actionExit.triggered.connect(self.exitCall)
        self.actionSettings.triggered.connect(self.SettingsWindow)
        
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
        
    def exitCall(self):
        print("Kill application....")
        serialComHandler.close()
        sys.exit()
        
    def SettingsWindow(self):
       

       self.window = QtWidgets.QMainWindow()
       self.ui = Settings.Ui_SettingsWindow()
       self.ui.setupUi(self.window)
       self.ui.ReadInitFile()
       self.ui.CheckButton()
       self.window.show()
       
       
    def ReadCommands(self, MainWindow):
        self.listWidget.clear()
        self.listWidget.setStyleSheet("font: 8pt Comic Sans MS")
        if (self.comboBox.currentIndex() == 0):
            with open('SupportedCommands.txt','r') as commandsFile:
                for commands in commandsFile:
                    self.listWidget.addItem(commands)
        else:
                self.listWidget.clear()
                      
    def SendCommand(self, MainWindow):
        items = self.listWidget.selectedItems()
        if items and stillConnected:
            self.textBrowser.clear()
            self.textBrowser.append(self.listWidget.currentItem().text())
            word_list = self.listWidget.currentItem().text().split()
            
            global detectChanges
            if Settings.detectChanges is True:
                serialComHandler.close()
                self.InitSerialCommunication()
                Settings.detectChanges = False
                
            if (FBL_GET_VERSION_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_GET_VERSION_CMD)
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
    
    def CommandTypeSelection(self,MainWindow):
        self.comboBox.currentIndexChanged.connect(self.ReadCommands)
    
    
    def CommandTypeSelection(self,MainWindow):
        self.comboBox.currentIndexChanged.connect(self.ReadCommands)
    
    def ParseInitFile(self):
         global serialCOM 
         global baudRate
         with open('InitFile.ini','r') as commandsFile:
             serialCOM = commandsFile.readlines()[1][12:16]
             commandsFile.seek(0)
             baudRate = commandsFile.readlines()[2]
             baudRate = baudRate.split('"')[1]
             
    def InitSerialCommunication(self):
        global serialComHandler
        global init_done
        global stillConnected
        #print ("CALL")
        self.ParseInitFile()
      
        try:
                serialComHandler.close()
                serialComm = serial.Serial()
                serialComm.baudrate = baudRate
                serialComm.port = serialCOM
                serialComm.open()
                serialComHandler = serialComm
                if serialComm.is_open is True:
                    font=QtGui.QFont()
                    font.setBold(True)
                    color= QtGui.QPalette()
                    color.setColor(QtGui.QPalette.Text, QtCore.Qt.green)
                    self.textBrowser_2.setPalette(color)
                    self.textBrowser_2.setFont(font)
                    self.textBrowser_2.clear()
                    self.textBrowser.clear()
                    self.textBrowser_2.append("COM port opened")
                    #serialComm.write(b'Hello')
                    init_done = True
                    stillConnected = True
                  
        except:
                stillConnected = False
                myFont=QtGui.QFont()
                myFont.setBold(True)
                color= QtGui.QPalette()
                color.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
                self.textBrowser_2.setPalette(color)
                self.textBrowser_2.setFont(myFont)
                self.textBrowser_2.clear()
                self.textBrowser.clear()
                self.textBrowser_2.append("Error: Check communication port and other settings")
        
        
#       serialComm.port) = self.ui.GetComName()
      
       

#------------------------------COMMON-----------------------------------------
def word_to_byte(addr, index , lowerfirst):
    value = (addr >> ( 8 * ( index -1)) & 0x000000FF )
    return value

def get_crc(buff, length):
    Crc = 0xFFFFFFFF
    #print(length)
    for data in buff[0:length]:
        Crc = Crc ^ data
        for i in range(32):
            if(Crc & 0x80000000):
                Crc = (Crc << 1) ^ 0x04C11DB7
            else:
                Crc = (Crc << 1)
    return Crc
#-----------------------------------------------------------------------------

#----------------------------SERIAL-------------------------------------------
def read_serial_port(length):
    read_value = serialComHandler.read(length)
    return read_value

def Close_serial_port():
    pass
def purge_serial_port():
    serialComHandler.reset_input_buffer()
    
def Write_to_serial_port(self,value, *length):
    if stillConnected:
        data = struct.pack('>B', value)
        value = bytearray(data)
        output = "0x{:02x}".format(value[0])
        myFont=QtGui.QFont()
        myFont.setBold(True)
        color= QtGui.QPalette()
        color.setColor(QtGui.QPalette.Text, QtCore.Qt.black)
        self.textBrowser.setPalette(color)
        self.textBrowser.setFont(myFont)
        self.textBrowser.setText(self.textBrowser.toPlainText() + " " + output)
        serialComHandler.write(data)




#-----------------------------------------------------------------------------

#----------------------------HANDLE-------------------------------------------
def read_bootloader_reply(command_code):
    #ack=[0,0]
    len_to_follow=0 
    ret = -2 

    #read_serial_port(ack,2)
    #ack = ser.read(2)
    ack=read_serial_port(2)
    if(len(ack) ):
        a_array=bytearray(ack)
        #print("read uart:",ack) 
        if (a_array[0]== 0xA5):
            #CRC of last command was good .. received ACK and "len to follow"
            len_to_follow=a_array[1]
            print("\n   CRC : SUCCESS Len :",len_to_follow)
            #print("command_code:",hex(command_code))
            if (command_code) == FBL_GET_VERSION_CMD :
                #Receive_GetVersion(len_to_follow)
                a = 0
#            elif(command_code) == FBL_GET_HELP_CMD:
               # process_COMMAND_BL_GET_HELP(len_to_follow)
                
#            elif(command_code) == COMMAND_BL_GET_CID:
#                process_COMMAND_BL_GET_CID(len_to_follow)
#                
#            elif(command_code) == COMMAND_BL_GET_RDP_STATUS:
#                process_COMMAND_BL_GET_RDP_STATUS(len_to_follow)
#                
#            elif(command_code) == COMMAND_BL_GO_TO_ADDR:
#                process_COMMAND_BL_GO_TO_ADDR(len_to_follow)
#                
#            elif(command_code) == COMMAND_BL_FLASH_ERASE:
#                process_COMMAND_BL_FLASH_ERASE(len_to_follow)
#                
#            elif(command_code) == COMMAND_BL_MEM_WRITE:
#                process_COMMAND_BL_MEM_WRITE(len_to_follow)
#                
#            elif(command_code) == COMMAND_BL_READ_SECTOR_P_STATUS:
#                process_COMMAND_BL_READ_SECTOR_STATUS(len_to_follow)
#                
#            elif(command_code) == COMMAND_BL_EN_R_W_PROTECT:
#                process_COMMAND_BL_EN_R_W_PROTECT(len_to_follow)
#                
#            elif(command_code) == COMMAND_BL_DIS_R_W_PROTECT:
#                process_COMMAND_BL_DIS_R_W_PROTECT(len_to_follow)
#                
#            elif(command_code) == COMMAND_BL_MY_NEW_COMMAND:
#                process_COMMAND_BL_MY_NEW_COMMAND(len_to_follow)
#                
            else:
                print("\n   Invalid command code\n")
                
            ret = 0
         
        elif a_array[0] == 0x7F:
            #CRC of last command was bad .. received NACK
            print("\n   CRC: FAIL \n")
            ret= -1
    else:
        print("\n   Timeout : Bootloader not responding")
        
    return ret

def HandleCommands(self,command):
    ret_value = 0
    data_buf = []
    for i in range(255):
        data_buf.append(0)
    
    if(command  == 0 ):
        raise SystemExit
    elif(command == 1):
        #print("\n   Command == > BL_GET_VER")
        FBL_COMMAND_BL_GET_VER_LEN              = 6
        data_buf[0] = FBL_COMMAND_BL_GET_VER_LEN-1 
        data_buf[1] = int(FBL_GET_VERSION_CMD,16) 
        crc32       = get_crc(data_buf,FBL_COMMAND_BL_GET_VER_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[2] = word_to_byte(crc32,1,1) 
        data_buf[3] = word_to_byte(crc32,2,1) 
        data_buf[4] = word_to_byte(crc32,3,1) 
        data_buf[5] = word_to_byte(crc32,4,1) 

        
        Write_to_serial_port(self,data_buf[0],1)
        for i in data_buf[1:FBL_COMMAND_BL_GET_VER_LEN]:
            Write_to_serial_port(self,i,FBL_COMMAND_BL_GET_VER_LEN-1)
        

        #ret_value = read_bootloader_reply(data_buf[1])



#-----------------------------------------------------------------------------

        

import LogoLabel_rc
import Usb_rc

if __name__ == "__main__":
    import sys
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.ReadCommands(MainWindow)
    ui.CheckButton(MainWindow)
    ui.InitSerialCommunication()
    ui.CommandTypeSelection(MainWindow)
    MainWindow.show()
    app.exec_()

