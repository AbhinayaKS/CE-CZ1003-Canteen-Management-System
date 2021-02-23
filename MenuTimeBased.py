#This file has been written by KESARIMANGALAM SRINIVASAN ABHINAYA

from PyQt5 import QtCore, QtGui, QtWidgets
import check_store_open
import Menu_Read
from PyQt5.QtCore import QDateTime

#Obtaining the current date and time and converting it to a string
datetime = QDateTime.currentDateTime()
DateTime = datetime.toString()

#Obtaining the hour by first checking if the date is a single digit or double digit
#This is done because the DateTime string's format: Mon Nov 11 11:12:27 2019
hour = 0
if DateTime[9] == ' ':
    hour = int(DateTime[10:12]+DateTime[13:15])
else:
    hour = int(DateTime[11:13]+DateTime[14:16])

#Obtaining the day from the string
day = DateTime[0:3]
    
#Creating an empty list to hold the list of open stalls
Open_List = []

class Ui_Dialog(object):
    
    #Function to call the functions from Menu_Read file based on the option picked by the user - Written by CHENG ZHEN
    def disp(self,Dialog):
        Stall = self.Dropdown.currentText()
        if(Stall == "McDonalds"):
            self.Menu_Display.setText(Menu_Read.McDonalds_Time(hour))
        elif(Stall == "Chinese Stall"):
            self.Menu_Display.setText(Menu_Read.ChineseStall())
        elif(Stall == "Italian Stall"):
            self.Menu_Display.setText(Menu_Read.ItalianStall())
        elif(Stall == "Malay Stall"):
            self.Menu_Display.setText(Menu_Read.MalayStall())
        elif(Stall == "Indian Stall"):
            self.Menu_Display.setText(Menu_Read.IndianStall_Time(hour))
        else:
            self.Menu_Display.setText("")

    def setupUi(self, Dialog):
        #Creating a font
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        
        #Creating a window
        Dialog.setObjectName("Display Menu")
        Dialog.resize(400, 300)
        Dialog.setWindowTitle("Diaplay Menu")

        #Creating the background
        self.BG = QtWidgets.QLabel(Dialog)
        self.BG.setGeometry(QtCore.QRect(-4, -8, 411, 311))
        self.BG.setPixmap(QtGui.QPixmap("food_bg.jpg"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")

        #Creating the scrollable area to hold the different widgets                            
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 30, 421, 231))
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 229))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #Adding the Heading
        self.Heading = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Heading.setGeometry(QtCore.QRect(20, 30, 301, 21))
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")

        #Creating a dropdown to display the list of Stalls that are available for the user to pick
        self.Dropdown = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.Dropdown.setGeometry(QtCore.QRect(120, 70, 121, 22))
        self.Dropdown.setObjectName("Dropdown")
        self.Dropdown.addItem("")
        self.Dropdown.setItemText(0, "")

        #Adding a submit button
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(270, 70, 75, 23))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        #Creating a label for displaying the menu
        self.Menu_Display = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Menu_Display.setGeometry(QtCore.QRect(60, 100, 271, 131))
        self.Menu_Display.setFont(font)
        self.Menu_Display.setObjectName("Menu_Display")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Adding the data to the label and connecting the button to the function
        self.Heading.setText("Pick the restaurant to view the menu: ")
        self.pushButton.setText("Submit")
        self.pushButton.clicked.connect(self.disp)

        #Adding items to the dropdown based on the List obtained of the open restaurants at the moment
        j=1
        for i in Open_List:
            i = i[:len(i)-1]
            self.Dropdown.addItem("")
            self.Dropdown.setItemText(j,i)
            j = j + 1

def mainfunc(h = 0,d = '\0'):
    global Open_List

    #If a parameter is passed indicating that it needs to run based on a manual time, it is set to the previously declared global variable
    if h:
        global hour,day
        hour = h
        day = d

    #Obtaining a list of open stalls at the specified time
    Open_List = check_store_open.Stalls_Open(day,hour)
    
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.exec_()
