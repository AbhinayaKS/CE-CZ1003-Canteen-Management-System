#This file has been written by CHENG ZHEN
def McDonalds_Time(hour):
    McD = ""

    #Reading from the file
    myfile = open("McDonalds.txt", "r")
    Full_Menu = myfile.readlines()

    #Deciding between the morning and the evening menu
    if hour <= 1200:
        start = 0
        end = 2
    else:
        start = 2
        end = 4

    #Loop to get the data from the file and store it in a string    
    j=1
    for i in range(start,end):
        McD = McD + str(j) + ") " + Full_Menu[i]
        j=j+1
        
    myfile.close()

    #Returning the string
    return McD

def McDonalds():
    #Function to dislay the entire Menu of McD rather than time based
    McD = ""

    #Reading from the file
    myfile = open("McDonalds.txt", "r")
    Full_Menu = myfile.readlines()

    #Storing the data in a string in the required format to be displayed
    for i in range(0,4):
        McD = McD + str(i+1) + ") " + Full_Menu[i]
        
    myfile.close()

    #Returning the string
    return McD

def ChineseStall():
    Chinese = ""

    #Reading from the file
    myfile = open("Chinese.txt", "r")
    Full_Menu = myfile.readlines()

    #Storing the data in a string in the required format to be displayed
    for i in range(0,2):
       Chinese = Chinese + str(i+1) + ") " + Full_Menu[i]
       
    myfile.close()

    #Returning the string
    return Chinese

def MalayStall():
    Malay = ""

    #Reading from the file
    myfile = open("Malay.txt", "r")
    Full_Menu = myfile.readlines()

    #Storing the data in a string in the required format to be displayed
    for i in range(0,2):
        Malay = Malay + str(i+1) + ") " + Full_Menu[i]
        
    myfile.close()

    #Returning the string
    return Malay

def IndianStall():
    #Function to dislay the entire Menu of Indian Stall rather than time based
    Indian = ""

    #Reading from the file
    myfile = open("Indian.txt", "r")
    Full_Menu = myfile.readlines()
    
    #Storing the data in a string in the required format to be displayed
    for i in range(0,3):
        Indian = Indian + str(i+1) + ") " + Full_Menu[i]

    myfile.close()

    #Returning the string
    return Indian

def IndianStall_Time(hour):
    Indian = ""

    #Reading from the file
    myfile = open("Indian.txt", "r")
    Full_Menu = myfile.readlines()

    #Deciding between the morning and the evening menu
    if hour <= 1200:
        start = 0
        end = 1
    else:
        start = 1
        end = 3

    #Loop to get the data from the file and store it in a string    
    j=1
    for i in range(start,end):
        Indian = Indian + str(j) + ") " + Full_Menu[i]
        j=j+1
        
    myfile.close()

    #Returning the string
    return Indian

def ItalianStall():
    Italian = ""

    #Reading from the file
    myfile = open("Italian.txt", "r")
    Full_Menu = myfile.readlines()

    #Storing the data in a string in the required format to be displayed
    for i in range(0,3):
        Italian = Italian + str(i+1) + ") " + Full_Menu[i]
        
    myfile.close()

    #Returning the string
    return Italian
