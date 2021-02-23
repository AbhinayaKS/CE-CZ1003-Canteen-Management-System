#This file has been written by KESARIMANGALAM SRINIVASAN ABHINAYA

from PyQt5 import QtCore, QtGui, QtWidgets
import check_store_open

a = check_store_open.Operating_Hours()

class Ui_OperatingHours(object):

    def setupUi(self, OperatingHours):

        #Creating Window
        OperatingHours.setObjectName("OperatingHours")
        OperatingHours.resize(841, 528)
        OperatingHours.setWindowTitle("Operating Hours")

        #Creating a scroll area and widget contents to display the content
        self.scrollArea = QtWidgets.QScrollArea(OperatingHours)
        self.scrollArea.setGeometry(QtCore.QRect(0, 40, 841, 451))
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -555, 822, 1004))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        #Creating a grid in the window for organisation
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        #Creating a font for the content and the heading
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        fontH = QtGui.QFont()
        fontH.setFamily("Times New Roman")
        fontH.setPointSize(14)

        #Adding the Logos, Headings and Content
        self.Heading = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Heading.setFont(fontH)
        self.Heading.setObjectName("Heading")
        self.gridLayout.addWidget(self.Heading, 1, 0, 1, 1)
        
        self.McD_Logo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.McD_Logo.setPixmap(QtGui.QPixmap("McD.png"))
        self.McD_Logo.setObjectName("McD_Logo")
        self.gridLayout.addWidget(self.McD_Logo, 3, 0, 1, 1)

        self.McD_OH = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.McD_OH.setFont(font)
        self.McD_OH.setObjectName("McD_OH")
        self.gridLayout.addWidget(self.McD_OH, 4, 0, 1, 1)
        
        self.Italian_Logo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Italian_Logo.setPixmap(QtGui.QPixmap("Italian Stall.png"))
        self.Italian_Logo.setObjectName("Italian_Logo")
        self.gridLayout.addWidget(self.Italian_Logo, 9, 0, 1, 1)

        self.Italian_OH = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Italian_OH.setFont(font)
        self.Italian_OH.setObjectName("Italian_OH")
        self.gridLayout.addWidget(self.Italian_OH, 10, 0, 1, 1)
        
        self.India_Logo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.India_Logo.setPixmap(QtGui.QPixmap("Indian Stall.png"))
        self.India_Logo.setObjectName("India_Logo")
        self.gridLayout.addWidget(self.India_Logo, 6, 0, 1, 1)

        self.Indian_OH = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Indian_OH.setFont(font)
        self.Indian_OH.setObjectName("Indian_OH")
        self.gridLayout.addWidget(self.Indian_OH, 7, 0, 1, 1)
        
        self.Malay_Logo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Malay_Logo.setPixmap(QtGui.QPixmap("Malay Stall.png"))
        self.Malay_Logo.setObjectName("Malay_Logo")
        self.gridLayout.addWidget(self.Malay_Logo, 6, 2, 1, 1)
        
        self.Malay_OH = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Malay_OH.setFont(font)
        self.Malay_OH.setObjectName("Malay_OH")
        self.gridLayout.addWidget(self.Malay_OH, 7, 2, 1, 1)
        
        self.Chinese_Logo = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Chinese_Logo.setPixmap(QtGui.QPixmap("Chinese.png"))
        self.Chinese_Logo.setObjectName("Chinese_Logo")
        self.gridLayout.addWidget(self.Chinese_Logo, 3, 2, 1, 1)
        
        self.Chinese_OH = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Chinese_OH.setObjectName("Chinese_OH")
        self.Chinese_OH.setFont(font)
        self.gridLayout.addWidget(self.Chinese_OH, 4, 2, 1, 1)        

        self.BG = QtWidgets.QLabel(OperatingHours)
        self.BG.setGeometry(QtCore.QRect(0, 0, 841, 531))
        self.BG.setPixmap(QtGui.QPixmap("food_bg.jpg"))
        self.BG.setObjectName("BG")
        self.BG.setScaledContents(True)
        self.BG.raise_()
        self.scrollArea.raise_()

        QtCore.QMetaObject.connectSlotsByName(OperatingHours)

        #Adding the text to be displayed
        self.McD_OH.setText("".join(a[0]))
        self.Heading.setText("Operating Hours:")
        self.Italian_OH.setText("".join(a[4]))
        self.Indian_OH.setText("".join(a[3]))
        self.Malay_OH.setText("".join(a[2]))
        self.Chinese_OH.setText("".join(a[1]))

        #Creating spaces for better presentability of the window
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 11, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 8, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)


def hours():
    OperatingHours = QtWidgets.QDialog()
    ui = Ui_OperatingHours()
    ui.setupUi(OperatingHours)
    OperatingHours.exec_()
