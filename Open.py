#This file has been written by KESARIMANGALAM SRINIVASAN ABHINAYA

from PyQt5 import QtCore, QtGui, QtWidgets
import check_store_open
import Menu_Read
from PyQt5.QtCore import QDateTime
import MenuTimeBased

#Obtaining the current date and time
datetime = QDateTime.currentDateTime()
DateTime = datetime.toString()
day = DateTime[0:3]

#Obtaining the hour by first checking if the date is a single digit or double digit
#This is done because the DateTime string's format: Mon Nov 11 11:12:27 2019
hour = 0
if DateTime[9] == ' ':
    hour = int(DateTime[10:12]+DateTime[13:15])
else:
    hour = int(DateTime[11:13]+DateTime[14:16])

#Obtaining the list of open restaurants
Open_List = check_store_open.Stalls_Open(day,hour)

#Converting the list to a string
Open_Str = "".join(Open_List)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        #Creating the fonts
        font1 = QtGui.QFont()
        font1.setFamily("Times New Roman")
        font1.setPointSize(14)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        
        #Creating a window
        Dialog.setObjectName("Dialog")
        Dialog.resize(552, 385)
        Dialog.setWindowTitle("Open Restaurants")

        #Creating a background
        self.BG = QtWidgets.QLabel(Dialog)
        self.BG.setGeometry(QtCore.QRect(0, 0, 551, 391))
        self.BG.setPixmap(QtGui.QPixmap("bg.png"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")

        #Creating a scrollable area to hold the different widgets
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 40, 580, 291))
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #Adding the heading
        self.Heading = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Heading.setGeometry(QtCore.QRect(20, 50, 371, 16))
        self.Heading.setFont(font1)
        self.Heading.setObjectName("Heading")

        #Displaying the current time
        self.Time = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Time.setGeometry(QtCore.QRect(370, 20, 200, 20))
        self.Time.setFont(font)
        self.Time.setObjectName("Time")
        
        #Creating a list area to list he available restaurants
        self.List = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.List.setGeometry(QtCore.QRect(46, 92, 250, 171))
        self.List.setFont(font1)
        self.List.setObjectName("List")

        #Adding a menu button for the user to view the time based menu
        self.MenuButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.MenuButton.setGeometry(QtCore.QRect(330, 130, 170, 61))
        self.MenuButton.setObjectName("MenuButton")
        self.MenuButton.setFont(font1)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #Adding the data to be displayed and connecting the button to the function
        self.Heading.setText("The available restaurants at the moment are: ")
        self.Time.setText(DateTime)
        self.List.setText(Open_Str)
        self.MenuButton.setText("View Menu based \n on the current Time")
        self.MenuButton.clicked.connect(MenuTimeBased.mainfunc)

def Open():
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.exec_()
