#This file has been written by LEE LUCIUS

def validate_month(month): #validate the month
    try:
        int(month)
    except:
        return False
    else:
        if int(month)<1 or int(month)>12:
            return False
        else:
            return True

def validate_date(date,month): #validate date of month
    month_dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}#dictionary for month
    try:
        int(date)
    except:
        return False #return False if not integer
    else:
        if int(date)<1 or int(date)>month_dict[int(month)]: #check if date is within month days
            return False
        else:
            return True

def validate_year(year): #validate year,from present year to 50 years later
    import datetime
    current_year=int(datetime.datetime.now().year)
    try:
        int(year)
    except:
        return False
    else:
        if int(year)<current_year or int(year)>(current_year+50):
            return False
        else:
            return True
        
def validate_time(time): #argument is time in 24hr clock
    try:
        int(time)
    except:
        return False
    else:
        if int(time)<0 or int(time)>2359:
            return False
        else:
            return True

def get_day(date,month,year): #arguments are validated date, month and year
    import datetime
    import calendar
    day = calendar.day_name[datetime.datetime(year,month,date).weekday()][0:3]
    return day
