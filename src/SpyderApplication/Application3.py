# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Application.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import serial
import struct
import os
import time

saveHandler = False
init_done = False
stillConnected = False

binaryFile=""

serialCOM = ""
baudRate = ""
goToAddress = ""
memoryWriteAddress = ""
payload = ""
memoryReadAddress = ""
readLength = ""
sectorNumber = ""
numberofSectors = ""
sectorsProtected = ""
protectionModes = ""

serialComHandler = serial.Serial()
import Settings
from PyQt5 import QtCore, QtGui, QtWidgets

FBL_PROGRAM_FLASH = "0x00"
FBL_INTERNAL_PROGRAM_FLASH = 13
FBL_STREAM_SIZE = 128
FBL_GET_VERSION_CMD = "0x14"
FBL_INTERNAL_GET_VERSION_CMD = 1
FBL_GET_HELP_CMD = "0x22"
FBL_INTERNAL_GET_HELP_CMD = 2
FBL_GET_CID_CMD = "0x44"
FBL_INTERNAL_GET_CID_CMD = 3
FBL_GET_RDP_LEVEL_CMD = "0x25"
FBL_INTERNAL_GET_RDP_LEVEL_CMD = 4
FBL_GO_TO_ADDR_CMD = "0x19"
FBL_INTERNAL_GO_TO_ADDR_CMD = 5
FBL_ERASE_FLASH_CMD = "0x84"
FBL_INTERNAL_ERASE_FLASH_CMD= 6
FBL_MEMORY_WRITE_CMD = "0x32"
FBL_INTERNAL_MEMORY_WRITE_CMD = 7
FBL_ENABLE_RW_PROTECTION_CMD = "0x3C"
FBL_INTERNAL_ENABLE_RW_PROTECTION_CMD = 8
FBL_MEMORY_READ_CMD = "0x2B"
FBL_INTERNAL_MEMORY_READ_CMD = 9
FBL_READ_SECTOR_PROTECTION_STATUS_CMD = "0x78"
FBL_INTERNAL_READ_SECTOR_PROTECTION_STATUS_CMD = 10
FBL_READ_OTP_CMD = "0x1F"
FBL_INTERNAL_READ_OTP_CMD = 11
FBL_DISABLE_RW_PROTECTION_CMD = "0x6C"
FBL_INTERNAL_DISABLE_RW_PROTECTION_CMD = 12



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
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_GET_HELP_CMD)
            elif (FBL_GET_CID_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_GET_CID_CMD)
            elif (FBL_GET_RDP_LEVEL_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_GET_RDP_LEVEL_CMD)
            elif (FBL_GO_TO_ADDR_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_GO_TO_ADDR_CMD)
            elif (FBL_ERASE_FLASH_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_ERASE_FLASH_CMD)
            elif (FBL_MEMORY_WRITE_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_MEMORY_WRITE_CMD)
            elif (FBL_ENABLE_RW_PROTECTION_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_ENABLE_RW_PROTECTION_CMD)
            elif (FBL_MEMORY_READ_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_MEMORY_READ_CMD)
            elif (FBL_READ_SECTOR_PROTECTION_STATUS_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_READ_SECTOR_PROTECTION_STATUS_CMD)
            elif (FBL_READ_OTP_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_READ_OTP_CMD)
            elif (FBL_DISABLE_RW_PROTECTION_CMD == word_list[-1]):
                #self.textBrowser.append(word_list[-1])
                HandleCommands(self,FBL_INTERNAL_DISABLE_RW_PROTECTION_CMD) 
            elif (FBL_PROGRAM_FLASH == word_list[-1]):
                HandleCommands(self,FBL_INTERNAL_PROGRAM_FLASH) 
            else:
                HandleCommands(self,0) 
            
            
        
            
    def ProgrammingMessage(self):
         self.OpenBinaryFile()
         fileSize = self.GetBinaryFileSize()
         concatenatedString = "File size: " + str(fileSize) + " bytes."
         self.textBrowser.append(concatenatedString)
         font=QtGui.QFont()
         font.setBold(True)
         color= QtGui.QPalette()
         color.setColor(QtGui.QPalette.Text, QtCore.Qt.green)
         self.textBrowser_2.setPalette(color)
         self.textBrowser_2.setFont(font)
         self.textBrowser_2.clear()
         self.textBrowser_2.append("Binary file uploaded ")
                     
    def CheckButton(self, MainWindow):
        self.pushButton.clicked.connect(self.SendCommand)
    
    def CommandTypeSelection(self,MainWindow):
        self.comboBox.currentIndexChanged.connect(self.ReadCommands)
    
    
    def CommandTypeSelection(self,MainWindow):
        self.comboBox.currentIndexChanged.connect(self.ReadCommands)
    
    def ParseInitFile(self):
         global serialCOM
         global baudRate
         global sectorNumber
         global numberofSectors
         global goToAddress
         global memoryReadAddress
         global readLength
         global sectorsProtected
         global protectionModes
         global memoryWriteAddress
         global payload
         with open('InitFile.ini','r') as commandsFile:
             serialCOM = commandsFile.readlines()[1][12:16]
             commandsFile.seek(0)
             baudRate = commandsFile.readlines()[2]
             baudRate = baudRate.split('"')[1]
             commandsFile.seek(0)
             sectorNumber = commandsFile.readlines()[9]
             sectorNumber = sectorNumber.split('"')[1]
             commandsFile.seek(0)
             numberofSectors = commandsFile.readlines()[10]
             numberofSectors = numberofSectors.split('"')[1]
             commandsFile.seek(0)
             goToAddress = commandsFile.readlines()[5]
             goToAddress = goToAddress.split('"')[1]
             commandsFile.seek(0)
             memoryReadAddress = commandsFile.readlines()[7]
             memoryReadAddress = memoryReadAddress.split('"')[1]
             commandsFile.seek(0)
             readLength = commandsFile.readlines()[8]
             readLength = readLength.split('"')[1]
             commandsFile.seek(0)
             sectorsProtected = commandsFile.readlines()[14]
             sectorsProtected = sectorsProtected.split('"')[1]
             commandsFile.seek(0)
             protectionModes = commandsFile.readlines()[16]
             protectionModes = protectionModes.split('"')[1]
             commandsFile.seek(0)
             memoryWriteAddress = commandsFile.readlines()[6]
             memoryWriteAddress = memoryWriteAddress.split('"')[1]
             commandsFile.seek(0)
             payload = commandsFile.readlines()[11]
             payload = payload.split('"')[1]
             commandsFile.seek(0)
             
    def OpenBinaryFile(self):
        global binaryFile
        with open('InitFile.ini','r') as commandsFile:
            directoryFile = commandsFile.readlines()[12]
            directoryFile = directoryFile.split('"')[1]
        binaryFile = open (directoryFile,'rb')
    def CloseBinaryFile(self):
        binaryFile.close()
    def GetBinaryFileSize(self):
        with open('InitFile.ini','r') as commandsFile:
            directoryFile = commandsFile.readlines()[12]
            directoryFile = directoryFile.split('"')[1]
        size = os.path.getsize(directoryFile)
        return size
    
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
    
def Write_to_serial_port(self,value):
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
        #print("send")
        
def Flash_to_serial_port(self,value):
    if stillConnected:
        data = struct.pack('>B', value)
        serialComHandler.write(data)
        #print("send")



#-----------------------------------------------------------------------------

#----------------------------HANDLE-------------------------------------------
def read_bootloader_reply(self,command_code):
    #ack=[0,0]
    len_to_follow=0 
    ret = -2 

    #read_serial_port(ack,2)
    #ack = ser.read(2)
    ack=read_serial_port(20)
    if(len(ack)):
        a_array=bytearray(ack)
        self.textBrowser_2.clear()
        self.textBrowser_2.append("Dummy data received")
        
        print(ack)
        if (a_array[0]== 0xA5):
            #CRC of last command was good .. received ACK and "len to follow"
            len_to_follow=a_array[1]
            print("\n   CRC : SUCCESS Len :",len_to_follow)
            #print("command_code:",hex(command_code))
            if (command_code == FBL_GET_VERSION_CMD) :
                #Receive_GetVersion(len_to_follow)
                a = 0
            elif(command_code == FBL_GET_HELP_CMD):
               # process_COMMAND_BL_GET_HELP(len_to_follow)
               a = 0 
            elif(command_code == FBL_GET_CID_CMD):
               # process_COMMAND_BL_GET_CID(len_to_follow)
               a = 0
            elif(command_code == FBL_GET_RDP_LEVEL_CMD):
                #process_COMMAND_BL_GET_RDP_STATUS(len_to_follow)
                a = 0
            elif(command_code == FBL_GO_TO_ADDR_CMD):
               # process_COMMAND_BL_GO_TO_ADDR(len_to_follow)
                a = 0
            elif(command_code == FBL_ERASE_FLASH_CMD):
                #process_COMMAND_BL_FLASH_ERASE(len_to_follow)
                a = 0
            elif(command_code == FBL_MEMORY_WRITE_CMD):
                #process_COMMAND_BL_MEM_WRITE(len_to_follow)
                a = 0
            elif(command_code == FBL_ENABLE_RW_PROTECTION_CMD):
                #process_COMMAND_BL_READ_SECTOR_STATUS(len_to_follow)
                a = 0
            elif(command_code == FBL_MEMORY_READ_CMD):
                #process_COMMAND_BL_EN_R_W_PROTECT(len_to_follow)
                a = 0
            elif(command_code == FBL_READ_SECTOR_PROTECTION_STATUS_CMD):
                #process_COMMAND_BL_DIS_R_W_PROTECT(len_to_follow)
                a = 0
            elif(command_code == FBL_READ_OTP_CMD):
                #process_COMMAND_BL_MY_NEW_COMMAND(len_to_follow)
                a = 0
            elif(command_code == FBL_DISABLE_RW_PROTECTION_CMD):
                #process_COMMAND_BL_MY_NEW_COMMAND(len_to_follow)
                a = 0
            else:
                myFont=QtGui.QFont()
                myFont.setBold(True)
                color= QtGui.QPalette()
                color.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
                self.textBrowser_2.setPalette(color)
                self.textBrowser_2.setFont(myFont)
                self.textBrowser_2.clear()
                self.textBrowser_2.append(" Invalid command code. ")
                
            ret = 0
         
        elif a_array[0] == 0x7F:
            #CRC of last command was bad .. received NACK
            myFont=QtGui.QFont()
            myFont.setBold(True)
            color= QtGui.QPalette()
            color.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
            self.textBrowser_2.setPalette(color)
            self.textBrowser_2.setFont(myFont)
            self.textBrowser_2.clear()
            self.textBrowser_2.append(" CRC: FAIL ")
            ret= -1
    else:
         
          myFont=QtGui.QFont()
          myFont.setBold(True)
          color= QtGui.QPalette()
          color.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
          self.textBrowser_2.setPalette(color)
          self.textBrowser_2.setFont(myFont)
          self.textBrowser_2.clear()
          self.textBrowser_2.append("Timeout : Bootloader not responding")
    return ret

def HandleCommands(self,command):
    retValue = 0
    data_buf = []
    for i in range(255):
        data_buf.append(0)
    serialComHandler.timeout = 0.3;
    if(command  == 0 ):
        raise SystemExit
    elif(command == FBL_INTERNAL_GET_VERSION_CMD):
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
        for i in data_buf[0:FBL_COMMAND_BL_GET_VER_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
        retValue = read_bootloader_reply(self,data_buf[1])
    elif(command == FBL_INTERNAL_GET_HELP_CMD):
        
        FBL_COMMAND_BL_GET_HELP_CMD_LEN = 6
        data_buf[0] = FBL_COMMAND_BL_GET_HELP_CMD_LEN - 1
        data_buf[1] = int(FBL_GET_HELP_CMD,16)
        crc32 =  get_crc(data_buf,FBL_COMMAND_BL_GET_HELP_CMD_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[2] = word_to_byte(crc32,1,1) 
        data_buf[3] = word_to_byte(crc32,2,1) 
        data_buf[4] = word_to_byte(crc32,3,1) 
        data_buf[5] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_BL_GET_HELP_CMD_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
         
        retValue = read_bootloader_reply(self,data_buf[1])
    elif(command == FBL_INTERNAL_GET_CID_CMD):
        
        FBL_COMMAND_BL_GET_CID_CMD_LEN = 6
        data_buf[0] = FBL_COMMAND_BL_GET_CID_CMD_LEN - 1
        data_buf[1] = int(FBL_GET_CID_CMD,16)
        crc32 =  get_crc(data_buf,FBL_COMMAND_BL_GET_CID_CMD_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[2] = word_to_byte(crc32,1,1) 
        data_buf[3] = word_to_byte(crc32,2,1) 
        data_buf[4] = word_to_byte(crc32,3,1) 
        data_buf[5] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_BL_GET_CID_CMD_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
         
        retValue = read_bootloader_reply(self,data_buf[1])
    elif(command == FBL_INTERNAL_GET_RDP_LEVEL_CMD):
        
        FBL_COMMAND_BL_GET_RDP_CMD_LEN = 6
        data_buf[0] = FBL_COMMAND_BL_GET_RDP_CMD_LEN - 1
        data_buf[1] = int(FBL_GET_RDP_LEVEL_CMD,16)
        crc32 =  get_crc(data_buf,FBL_COMMAND_BL_GET_RDP_CMD_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[2] = word_to_byte(crc32,1,1) 
        data_buf[3] = word_to_byte(crc32,2,1) 
        data_buf[4] = word_to_byte(crc32,3,1) 
        data_buf[5] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_BL_GET_RDP_CMD_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
         
        retValue = read_bootloader_reply(self,data_buf[1])
    elif(command == FBL_INTERNAL_GO_TO_ADDR_CMD):
        
        FBL_COMMAND_GO_TO_ADDRESS_LEN = 10
        data_buf[0] = FBL_COMMAND_GO_TO_ADDRESS_LEN - 1
        data_buf[1] = int(FBL_GO_TO_ADDR_CMD,16)
        temp = int(goToAddress,16)
        data_buf[2] = word_to_byte(temp,1,1)
        data_buf[3] = word_to_byte(temp,2,1)
        data_buf[4] = word_to_byte(temp,3,1)
        data_buf[5] = word_to_byte(temp,4,1)
        crc32 =  get_crc(data_buf,FBL_COMMAND_GO_TO_ADDRESS_LEN-4)
        crc32 = crc32 & 0xffffffff
        #print(hex(crc32))
        print(word_to_byte(crc32,1,1) )
        data_buf[6] = word_to_byte(crc32,1,1) 
        data_buf[7] = word_to_byte(crc32,2,1) 
        data_buf[8] = word_to_byte(crc32,3,1) 
        data_buf[9] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_GO_TO_ADDRESS_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
         
        retValue = read_bootloader_reply(self,data_buf[1]) 
    elif(command == FBL_INTERNAL_ERASE_FLASH_CMD):
        
        FBL_COMMAND_BL_FLASH_ERASE_LEN = 8
        data_buf[0] = FBL_COMMAND_BL_FLASH_ERASE_LEN - 1
        data_buf[1] = int(FBL_ERASE_FLASH_CMD,16)
        data_buf[2] = int(sectorNumber,16)
        data_buf[3] = int(numberofSectors,16)
        crc32 =  get_crc(data_buf,FBL_COMMAND_BL_FLASH_ERASE_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[4] = word_to_byte(crc32,1,1) 
        data_buf[5] = word_to_byte(crc32,2,1) 
        data_buf[6] = word_to_byte(crc32,3,1) 
        data_buf[7] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_BL_FLASH_ERASE_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
         
        retValue = read_bootloader_reply(self,data_buf[1])
    elif(command == FBL_INTERNAL_MEMORY_WRITE_CMD):
        
        FBL_COMMAND_WRITE_TO_MEMORY_LEN = 15
        data_buf[0] = FBL_COMMAND_WRITE_TO_MEMORY_LEN - 1
        data_buf[1] = int(FBL_MEMORY_WRITE_CMD,16)
        temp1 = int(memoryWriteAddress,16)
        data_buf[2] = word_to_byte(temp1,1,1)
        data_buf[3] = word_to_byte(temp1,2,1)
        data_buf[4] = word_to_byte(temp1,3,1)
        data_buf[5] = word_to_byte(temp1,4,1)
        data_buf[6] = 4
        temp2 = int(payload,16)
        data_buf[7] = word_to_byte(temp2,1,1)
        data_buf[8] = word_to_byte(temp2,2,1)
        data_buf[9] = word_to_byte(temp2,3,1)
        data_buf[10] = word_to_byte(temp2,4,1)
        crc32 =  get_crc(data_buf,FBL_COMMAND_WRITE_TO_MEMORY_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[11] = word_to_byte(crc32,1,1) 
        data_buf[12] = word_to_byte(crc32,2,1) 
        data_buf[13] = word_to_byte(crc32,3,1) 
        data_buf[14] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_WRITE_TO_MEMORY_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
         
        retValue = read_bootloader_reply(self,data_buf[1])     
    elif(command == FBL_INTERNAL_ENABLE_RW_PROTECTION_CMD):
        
        FBL_COMMAND_ENABLE_RW_LEN = 8
        data_buf[0] = FBL_COMMAND_ENABLE_RW_LEN - 1
        data_buf[1] = int(FBL_ENABLE_RW_PROTECTION_CMD,16)
        data_buf[2] = int(sectorsProtected,16)
        data_buf[3] = int(protectionModes,16)
        crc32 =  get_crc(data_buf,FBL_COMMAND_ENABLE_RW_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[4] = word_to_byte(crc32,1,1) 
        data_buf[5] = word_to_byte(crc32,2,1) 
        data_buf[6] = word_to_byte(crc32,3,1) 
        data_buf[7] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_ENABLE_RW_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
         
        retValue = read_bootloader_reply(self,data_buf[1])     
    elif(command == FBL_INTERNAL_MEMORY_READ_CMD):
        
        FBL_COMMAND_MEMORY_READ_LEN = 11
        data_buf[0] = FBL_COMMAND_MEMORY_READ_LEN - 1
        data_buf[1] = int(FBL_MEMORY_READ_CMD,16)
        temp = int(memoryReadAddress,16)
        data_buf[2] = word_to_byte(temp,1,1)
        data_buf[3] = word_to_byte(temp,2,1)
        data_buf[4] = word_to_byte(temp,3,1)
        data_buf[5] = word_to_byte(temp,4,1)
        data_buf[6] = int(readLength,16)
        crc32 =  get_crc(data_buf,FBL_COMMAND_MEMORY_READ_LEN-4)
        crc32 = crc32 & 0xffffffff
        #print(hex(crc32))
        print(word_to_byte(crc32,1,1) )
        data_buf[7] = word_to_byte(crc32,1,1) 
        data_buf[8] = word_to_byte(crc32,2,1) 
        data_buf[9] = word_to_byte(crc32,3,1) 
        data_buf[10] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_MEMORY_READ_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
         
        retValue = read_bootloader_reply(self,data_buf[1]) 
    elif(command == FBL_INTERNAL_READ_SECTOR_PROTECTION_STATUS_CMD):
        
        FBL_COMMAND_BL_READ_SECTOR_STATUS_CMD_LEN = 6
        data_buf[0] = FBL_COMMAND_BL_READ_SECTOR_STATUS_CMD_LEN - 1
        data_buf[1] = int(FBL_READ_SECTOR_PROTECTION_STATUS_CMD,16)
        crc32 =  get_crc(data_buf,FBL_COMMAND_BL_READ_SECTOR_STATUS_CMD_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[2] = word_to_byte(crc32,1,1) 
        data_buf[3] = word_to_byte(crc32,2,1) 
        data_buf[4] = word_to_byte(crc32,3,1) 
        data_buf[5] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_BL_READ_SECTOR_STATUS_CMD_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
    elif(command == FBL_INTERNAL_READ_OTP_CMD):
        
        FBL_COMMAND_BL_READ_OTP_CMD_LEN = 6
        data_buf[0] = FBL_COMMAND_BL_READ_OTP_CMD_LEN - 1
        data_buf[1] = int(FBL_READ_OTP_CMD,16)
        crc32 =  get_crc(data_buf,FBL_COMMAND_BL_READ_OTP_CMD_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[2] = word_to_byte(crc32,1,1) 
        data_buf[3] = word_to_byte(crc32,2,1) 
        data_buf[4] = word_to_byte(crc32,3,1) 
        data_buf[5] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_BL_READ_OTP_CMD_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
    elif(command == FBL_INTERNAL_DISABLE_RW_PROTECTION_CMD):
        
        FBL_COMMAND_BL_GET_DISABLE_RW_CMD_LEN = 6
        data_buf[0] = FBL_COMMAND_BL_GET_DISABLE_RW_CMD_LEN - 1
        data_buf[1] = int(FBL_DISABLE_RW_PROTECTION_CMD,16)
        crc32 =  get_crc(data_buf,FBL_COMMAND_BL_GET_DISABLE_RW_CMD_LEN-4)
        crc32 = crc32 & 0xffffffff
        data_buf[2] = word_to_byte(crc32,1,1) 
        data_buf[3] = word_to_byte(crc32,2,1) 
        data_buf[4] = word_to_byte(crc32,3,1) 
        data_buf[5] = word_to_byte(crc32,4,1) 
        for i in data_buf[0:FBL_COMMAND_BL_GET_DISABLE_RW_CMD_LEN]:
            #print(hex(i))
            Write_to_serial_port(self,i)
            
    elif (command == FBL_INTERNAL_PROGRAM_FLASH):
         FBL_COMMAND_WRITE_PROGRAM_FLASH_LEN = 11
         self.OpenBinaryFile()
         fileSize = self.GetBinaryFileSize()
         self.ProgrammingMessage()
         bytesToSend = fileSize
         chunkSize = FBL_STREAM_SIZE
         totalLength = chunkSize + 11
         data_buf = [None] * totalLength
         data_buf[1] = int(FBL_PROGRAM_FLASH,16);
         memoryAddress = int(memoryWriteAddress,16)
         data_buf[6] = FBL_STREAM_SIZE
        
         while(bytesToSend):
           
            if (bytesToSend >= FBL_STREAM_SIZE):
                     chunkSize = FBL_STREAM_SIZE
                     bytesToSend = bytesToSend - FBL_STREAM_SIZE
            else:
                     chunkSize = bytesToSend
                     bytesToSend = 0
            data_buf[2] = word_to_byte(memoryAddress,1,1)
            data_buf[3] = word_to_byte(memoryAddress,2,1)
            data_buf[4] = word_to_byte(memoryAddress,3,1)
            data_buf[5] = word_to_byte(memoryAddress,4,1)
            
            for i in range(chunkSize):
                readByte = binaryFile.read(1)
                readByte = bytearray(readByte)
                data_buf[7+i] = int(readByte[0])
            
            command_total_length = FBL_COMMAND_WRITE_PROGRAM_FLASH_LEN + chunkSize
            data_buf[0] = command_total_length - 1
            crc32 = get_crc(data_buf, chunkSize + 7)
            data_buf[7+chunkSize] = word_to_byte(crc32,1,1)
            data_buf[8+chunkSize] = word_to_byte(crc32,2,1)
            data_buf[9+chunkSize] = word_to_byte(crc32,3,1)
            data_buf[10+chunkSize] = word_to_byte(crc32,4,1)
            memoryAddress = memoryAddress + chunkSize
           
            for j in data_buf[0:(command_total_length-1)]:
                Flash_to_serial_port(self,j)
                #print(hex(j))
         
        
         #print (fileSize)
             
         
         
         
        # crc32 = get_crc(data_buf,commandLength-4)
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

