#Following functions written by LEE LUCIUS
def Operating_Hours():
    myfile= open('OperatingTimes.txt','r')  #open file for reading
    operating_time=myfile.readlines() #add each line in the file to a list
    full_times = [operating_time[i:i+5] for i in range(0, len(operating_time), 5)]
    #split list into sub-list of 5 elements, each sub-list represent each store
    Chinese_times=full_times[0] #set variable for each sub-list for clarity
    Malay_times=full_times[1]
    Indian_times=full_times[2]
    Italian_times=full_times[3]
    myfile.close() #close file
    return ["Open 24/7",Chinese_times,Malay_times,Indian_times,Italian_times]
    
def Stalls_Open(day,hour):
    myfile= open('OperatingTimes.txt','r')  #open file for reading
    operating_time=myfile.readlines() #add each line in the file to a list
    for i in range(len(operating_time)): #remove \n from each line
        operating_time[i]=operating_time[i][:-1] 
    full_times = [operating_time[i:i+5] for i in range(0, len(operating_time), 5)]
    #split list into sub-list of 5 elements, each sub-list represent each store
    Chinese_times=full_times[0] #set variable for each sub-list for clarity
    Malay_times=full_times[1]
    Indian_times=full_times[2]
    Italian_times=full_times[3]
    myfile.close() #close file
    
    def check_all_open(day,hour): #function to check if any store is open
    #parameter day as Mon,Tue,Wed,Thu,Fri,Sat,Sun
    #parameter hour using the 24 hour clock, eg. 7pm as 1900
        Chinese_open=check_chinese_open(day,hour)
        Malay_open=check_malay_open(day,hour) 
        Indian_open=check_indian_open(day,hour)
        Italian_open=check_italian_open(day,hour)
        List_open= ["McDonalds\n"]
        if Chinese_open:
            List_open.append("Chinese Stall\n")
        if Malay_open:
            List_open.append("Malay Stall\n")
        if Indian_open:
            List_open.append("Indian Stall\n")
        if Italian_open:
            List_open.append("Italian Stall\n")
        return List_open

    def check_chinese_open(day,hour): #function to check if chinese store is open, same process used for other stores
        hour=int(hour) #convert hours to integer
        if day in Chinese_times[1]: #check if it is a weekday
            if hour >= int(Chinese_times[2][0:4]) and hour <= int(Chinese_times[2][5:9]):
                return True #return True if hour given is within opening hours
            else:
                return False
        elif day in Chinese_times[3]: #check if it is a weekend
            if hour >= int(Chinese_times[4][0:4]) and hour <= int(Chinese_times[4][5:9]):
                return True #return True if hour given is within opening hours
            else:
                return False
        else:
            return False

    def check_malay_open(day,hour):
        if day in Malay_times[1]:
            if hour >= int(Malay_times[2][0:4]) and hour <= int(Malay_times[2][5:9]):
                return True
            else:
                return False
        elif day in Malay_times[3]:
            if hour >= int(Malay_times[4][0:4]) and hour <= int(Malay_times[4][5:9]):
                return True
            else:
                return False
        else:
            return False

    def check_indian_open(day,hour):
        if day in Indian_times[1]:
            if hour >= int(Indian_times[2][0:4]) and hour <= int(Indian_times[2][5:9]):
                return True
            else:
                return False
        elif day in Indian_times[3]:
            if hour >= int(Indian_times[4][0:4]) and hour <= int(Indian_times[4][5:9]):
                return True
            else:
                return False
        else:
            return False

    def check_italian_open(day,hour):
        if day in Italian_times[1]:
            if hour >= int(Italian_times[2][0:4]) and hour <= int(Italian_times[2][5:9]):
                return True
            else:
                return False
        elif day in Italian_times[3]:
            if hour >= int(Italian_times[4][0:4]) and hour <= int(Italian_times[4][5:9]):
                return True
            else:
                return False
        else:
            return False
        
    return check_all_open(day,hour)


