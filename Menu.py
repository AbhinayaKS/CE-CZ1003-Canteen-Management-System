#This file has been written by KESARIMANGALAM SRINIVASAN ABHINAYA

from PyQt5 import QtCore, QtGui, QtWidgets
import Menu_Read

class Ui_Dialog(object):
    #Displaying the menu based on the Stall picked by the user
    def dispmenu(self,Dialog):
        Stall = self.Dropdown.currentText()
        if(Stall == "McDonalds"):
            self.Menu_Display.setText(Menu_Read.McDonalds())
        elif(Stall == "Chinese Stall"):
            self.Menu_Display.setText(Menu_Read.ChineseStall())
        elif(Stall == "Italian Stall"):
            self.Menu_Display.setText(Menu_Read.ItalianStall())
        elif(Stall == "Malay Stall"):
            self.Menu_Display.setText(Menu_Read.MalayStall())
        elif(Stall == "Indian Stall"):
            self.Menu_Display.setText(Menu_Read.IndianStall())
        else:
            self.Menu_Display.setText("")

    def setupUi(self, Dialog):
        #Creating a font
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        
        #Creating the window
        Dialog.setObjectName("Display Menu")
        Dialog.resize(400, 300)
        Dialog.setWindowTitle("Display Menu")

        #Creating the background
        self.BG = QtWidgets.QLabel(Dialog)
        self.BG.setGeometry(QtCore.QRect(-4, -8, 411, 311))
        self.BG.setPixmap(QtGui.QPixmap("food_bg.jpg"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")

        #Creating the scroll area for displaying the different widgets
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 30, 421, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 229))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #Adding the heading
        self.Heading = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Heading.setGeometry(QtCore.QRect(20, 30, 301, 21))
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")

        #Creating a dropdown of the different stalls for the user to view their menu
        self.Dropdown = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.Dropdown.setGeometry(QtCore.QRect(120, 70, 121, 22))
        self.Dropdown.setObjectName("Dropdown")

        #Adding 6 items to the dropdown (including one blank field)
        for i in range(0,6):
            self.Dropdown.addItem("")

        #Creating a submit button
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(270, 70, 75, 23))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        #Creating an area to display the menu
        self.Menu_Display = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Menu_Display.setGeometry(QtCore.QRect(60, 100, 271, 131))
        self.Menu_Display.setFont(font)
        self.Menu_Display.setObjectName("Menu_Display")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #Adding the different Stall names to the dropdown and setting the various contents to be displayed
        self.Heading.setText("Pick the restaurant to view the menu:")
        self.Dropdown.setItemText(0, "")
        self.Dropdown.setItemText(1, "McDonalds")
        self.Dropdown.setItemText(2, "Chinese Stall")
        self.Dropdown.setItemText(3, "Italian Stall")
        self.Dropdown.setItemText(4, "Malay Stall")
        self.Dropdown.setItemText(5, "Indian Stall")
        self.pushButton.setText("Submit")
        self.Menu_Display.setText("")

        #Connecting the button to the function
        self.pushButton.clicked.connect(self.dispmenu)
        
def menu():
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.exec_()
