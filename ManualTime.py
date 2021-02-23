#This file has been written by KESARIMANGALAM SRINIVASAN ABHINAYA

from PyQt5 import QtCore, QtGui, QtWidgets
import MenuTimeBased
import validate_date
from PyQt5.QtWidgets import QMessageBox

dd_str = mm_str = yy_str = time_str = day = ""

class Ui_Dialog(object):
    
    #Function when the submit button is clicked to open the manual time based menu written by CHENG ZHEN
    def submitted(self,Dialog):
        #Reading the data entered by the user in the line edit fields
        dd_str = self.dd.text()
        mm_str = self.mm.text()
        yy_str = self.yy.text()
        time_str = self.hh.text() + self.mins.text()
        valid = 0

        #Validating the inputs
        if validate_date.validate_month(mm_str):
            if validate_date.validate_date(dd_str,mm_str):
                if validate_date.validate_year(yy_str):
                    if validate_date.validate_time(time_str):
                        valid = 1
                        
        if valid:
            #Opening Time based menu
            day = validate_date.get_day(int(dd_str),int(mm_str),int(yy_str))
            MenuTimeBased.mainfunc(int(time_str),day)
        else:
            #Displaying error message
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Invalid Input")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            
    def setupUi(self, Dialog):
        #Creating Window
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 353)
        Dialog.setWindowTitle("Manual Time")

        #Creating the background
        self.BG = QtWidgets.QLabel(Dialog)
        self.BG.setGeometry(QtCore.QRect(0, -10, 601, 361))
        self.BG.setPixmap(QtGui.QPixmap("bg.png"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")

        #Creating the scroll area to act as a container for the other widgets
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 601, 211))
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)

        #Creating a container for inputting the date, month and year
        self.Container = QtWidgets.QWidget()
        self.Container.setGeometry(QtCore.QRect(0, 0, 599, 209))
        self.Container.setObjectName("Container")

        #Creating a grid on the window
        self.gridLayout = QtWidgets.QGridLayout(self.Container)
        self.gridLayout.setObjectName("gridLayout")

        #Creating a frame
        self.frame_2 = QtWidgets.QFrame(self.Container)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        #Creating a font for the content and the button
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        fontB = QtGui.QFont()
        fontB.setFamily("Times New Roman")
        fontB.setPointSize(12)
        
        #Adding the input fields
        self.dd = QtWidgets.QLineEdit(self.frame_2)
        self.dd.setGeometry(QtCore.QRect(20, 0, 71, 27))
        self.dd.setFont(font)
        self.dd.setCursorPosition(0)
        self.dd.setObjectName("dd")
        
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(100, 0, 5, 27))
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.mm = QtWidgets.QLineEdit(self.frame_2)
        self.mm.setGeometry(QtCore.QRect(110, 0, 77, 27))
        self.mm.setFont(font)
        self.mm.setCursorPosition(0)
        self.mm.setObjectName("mm")
        
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(190, 0, 5, 27))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.yy = QtWidgets.QLineEdit(self.frame_2)
        self.yy.setGeometry(QtCore.QRect(200, 0, 91, 27))
        self.yy.setFont(font)
        self.yy.setCursorPosition(0)
        self.yy.setObjectName("yy")
        
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.Container)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        
        self.mins = QtWidgets.QLineEdit(self.Container)
        self.mins.setFont(font)
        self.mins.setCursorPosition(0)
        self.mins.setObjectName("mins")
        self.gridLayout.addWidget(self.mins, 2, 3, 1, 1)
        
        self.hh = QtWidgets.QLineEdit(self.Container)
        self.hh.setFont(font)
        self.hh.setCursorPosition(0)
        self.hh.setObjectName("hh")
        self.gridLayout.addWidget(self.hh, 2, 1, 1, 1)
        
        #Creating the button
        self.Submit = QtWidgets.QPushButton(self.Container)
        self.Submit.setFont(fontB)
        self.Submit.setObjectName("Submit")
        self.gridLayout.addWidget(self.Submit, 4, 0, 1, 1)

        #Adding the heading
        self.Heading = QtWidgets.QLabel(self.Container)
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")
        self.gridLayout.addWidget(self.Heading, 0, 0, 1, 1)  
    
        self.scrollArea.setWidget(self.Container)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Adding Text
        self.label.setText("/")
        self.label_2.setText("/")
        self.Submit.setText("Submit")
        self.Heading.setText("Enter the date and time in the following format: \n dd/mm/yyyy\n hh:mm (in the 24 hr format)")
        self.label_3.setText(":")
        self.Submit.clicked.connect(self.submitted)

        #Adding space for better organisation in the window
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)


def set_time():
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.exec_()
