#This file has been written by KESARIMANGALAM SRINIVASAN ABHINAYA
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    #Function to calculate the expected wait time - WRITTEN BY LEE LUCIUS
    def Calc(self,Dialog):
        Stall = self.DropDown.currentText()
        num_q = self.Number.value()
        time_per_person=0
        if Stall == "McDonalds":
            time_per_person=1
            self.Logo.setPixmap(QtGui.QPixmap("McD.png"))
        elif Stall == "Indian Stall":
            time_per_person=2
            self.Logo.setPixmap(QtGui.QPixmap("Indian Stall.png"))
        elif Stall == "Italian Stall":
            time_per_person=3
            self.Logo.setPixmap(QtGui.QPixmap("Italian Stall.png"))
        elif Stall == "Chinese Stall":
            time_per_person=2
            self.Logo.setPixmap(QtGui.QPixmap("Chinese.png"))
        elif Stall == "Malay Stall":
            time_per_person=3
            self.Logo.setPixmap(QtGui.QPixmap("Malay Stall.png"))
            
        #Displaying the calculated wait time
        self.label.setText("The average wait time at the \n stall is expected to be " + str(time_per_person*num_q) + " minutes. " )
            
    def setupUi(self, Dialog):
        #Creating a font
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        
        #Create window
        Dialog.setObjectName("Dialog")
        Dialog.resize(702, 469)
        Dialog.setWindowTitle("Calculate Wait Time")

        #Creating the background
        self.BG = QtWidgets.QLabel(Dialog)
        self.BG.setGeometry(QtCore.QRect(0, 0, 711, 481))
        self.BG.setPixmap(QtGui.QPixmap("food_bg.jpg"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")

        #Creating a scrollabel area to hold the widgets
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(-10, 40, 711, 381))
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 709, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #Adding the heading
        self.Heading = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Heading.setGeometry(QtCore.QRect(30, 22, 451, 31))
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")

        #Adding a dropdown for the user to pick a stall
        self.DropDown = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.DropDown.setGeometry(QtCore.QRect(420, 30, 171, 22))
        self.DropDown.setObjectName("DropDown")

        #Adding 6 items to the dropdown including a blank field
        for i in range(0,6):
            self.DropDown.addItem("")
        self.DropDown.setItemText(0, "")

        #Creating a sumbit button
        self.Submit = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Submit.setGeometry(QtCore.QRect(280, 120, 75, 23))
        self.Submit.setObjectName("Submit")

        #Creating a label to display the logo of the stall
        self.Logo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Logo.setGeometry(QtCore.QRect(50, 160, 281, 181))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")

        #Creating a label to ask the user to enter the no. of people waiting in line
        self.NoofPeople = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.NoofPeople.setGeometry(QtCore.QRect(30, 80, 301, 16))
        self.NoofPeople.setFont(font)
        self.NoofPeople.setObjectName("NoofPeople")

        #Creating an input field(QSpinBox) that will take in only integer values from 0 to 9
        self.Number = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.Number.setGeometry(QtCore.QRect(290, 80, 81, 22))
        self.Number.setObjectName("Number")

        #Creating a label to display the calculated wait time
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(390, 170, 291, 171))
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Addign the data to be displayed and linking the button to the function
        self.Heading.setText("Pick a Restaurant to compute the average wait time:")
        self.DropDown.setItemText(1, "McDonalds")
        self.DropDown.setItemText(2, "Italian Stall")
        self.DropDown.setItemText(3, "Indian Stall")
        self.DropDown.setItemText(4, "Malay Stall")
        self.DropDown.setItemText(5, "Chinese Stall")
        self.Submit.setText("Submit")
        self.Logo.setText("")
        self.NoofPeople.setText("Enter the no. of people in the line: ")
        self.label.setText("")
        self.Submit.clicked.connect(self.Calc)


def WaitTime():
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.exec_()
