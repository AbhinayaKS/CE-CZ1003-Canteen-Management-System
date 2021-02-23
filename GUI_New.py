#This file has been written by KESARIMANGALAM SRINIVASAN ABHINAYA

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
import Menu
import Hours
import WaitTimeNew
import Open
import ManualTime

#Obtaining the current date and time
datetime = QDateTime.currentDateTime()
DateTime = datetime.toString()

# Handle high resolution displays:
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Creating the fonts
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setFamily("Times New Roman")
        fontH = QtGui.QFont()
        fontH.setFamily("Monotype Corsiva")
        fontH.setItalic(True)
        
        #Creating the main window
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Creating a scrollable area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 1250, 580))
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -303, 872, 752))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #Creating a grid layout inside the scrollabel area for better organisation
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        #Adding the main heading
        self.Heading = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Heading.setObjectName("Heading")
        self.Heading.setFont(fontH)
        self.Heading.setScaledContents(True)
        self.gridLayout.addWidget(self.Heading, 2, 2, 1, 1)
        
        #Creating a label to describe the system
        self.Desc = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Desc.setObjectName("Desc")
        self.Desc.setFont(font)
        self.Desc.setScaledContents(True)
        self.gridLayout.addWidget(self.Desc, 3, 2, 1, 1)
       
        #Creating the different buttons for the user to access the different features of the GUI
        self.Button1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button1.setFont(font)
        self.Button1.setObjectName("Button1")
        self.gridLayout.addWidget(self.Button1, 6, 2, 1, 1)
        
        self.Button2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button2.setFont(font)
        self.Button2.setObjectName("Button2")
        self.gridLayout.addWidget(self.Button2, 7, 2, 1, 1)
        
        self.Button3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button3.setFont(font)
        self.Button3.setObjectName("Button3")
        self.gridLayout.addWidget(self.Button3, 8, 2, 1, 1)

        self.Button4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button4.setFont(font)
        self.Button4.setObjectName("Button4")
        self.gridLayout.addWidget(self.Button4, 9, 2, 1, 1)
         
        self.Button5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button5.setFont(font)
        self.Button5.setObjectName("Button5")
        self.gridLayout.addWidget(self.Button5, 10, 2, 1, 1)
        
        #Creating a label to display the current date and time
        self.DateTime = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.DateTime.setFont(font)
        self.DateTime.setObjectName("DateTime")
        self.gridLayout.addWidget(self.DateTime, 0, 4, 1, 1)
        
        #Adding the different images
        self.Cook = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Cook.setPixmap(QtGui.QPixmap("cook.jpg"))
        self.Cook.setObjectName("Cook")
        self.gridLayout.addWidget(self.Cook, 2, 4, 1, 1)
        
        self.NTU_Logo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.NTU_Logo.setPixmap(QtGui.QPixmap("ntu.png"))
        self.NTU_Logo.setObjectName("NTU_Logo")
        self.gridLayout.addWidget(self.NTU_Logo, 0, 0, 1, 1)
        
        self.NorthSpine = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.NorthSpine.setPixmap(QtGui.QPixmap("NorthSpine.jpg"))
        self.NorthSpine.setObjectName("NorthSpine")
        self.gridLayout.addWidget(self.NorthSpine, 2, 0, 1, 1)

        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1250, 700))
        self.Background.setPixmap(QtGui.QPixmap("bg.png"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        
        #Raising the various widgets
        self.Desc.raise_()
        self.NTU_Logo.raise_()
        self.NorthSpine.raise_()
        self.Button1.raise_()
        self.Button3.raise_()
        self.Heading.raise_()
        self.Cook.raise_()
        self.DateTime.raise_()
        self.Button2.raise_()
        self.Button4.raise_()
        self.Button5.raise_()
        self.Background.raise_()
        self.scrollArea.raise_()

        #Adding spaces for better readability
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 0, 1, 1)
        spacerItem4= QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 11, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 1)
        
        #Adding a status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        #Adding the data and text to be displayed
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Canteen Management System")
        self.Desc.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#555500;\">You can use this System to view the available restaurants at the current date and </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#555500;\">time or a manually entered date and time. This system can also be used to view </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#555500;\">the menu fo the different stalls. You will be able to calculate the waiting time </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#555500;\">at a particular stall when the number of people in the queue is entered.</span></p></body></html>"))
        self.Button5.setText("View Menus of Restaurants")
        self.Button2.setText("View Available Restaurants using Manual Time and Date")
        self.Button3.setText("View Operating Hours of Restaurants")
        self.DateTime.setText(DateTime)
        self.Button1.setText("View Available Restaurants using Current Time and Date")
        self.Heading.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">Canteen Management</span></p><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">System</span></p></body></html>"))
        self.Button4.setText("Calculate Average Wait Time")

        #Connecting the buttons to the different functions
        self.Button5.clicked.connect(Menu.menu)
        self.Button3.clicked.connect(Hours.hours)
        self.Button4.clicked.connect(WaitTimeNew.WaitTime)
        self.Button1.clicked.connect(Open.Open)
        self.Button2.clicked.connect(ManualTime.set_time)

def GUI_Part():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(1250,700)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
