from datetime import datetime

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def anniversary_date(date_str):
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    year = date_obj.year
    
    if is_leap_year(year):
        leap_status = "Leap Year"
        anniversary_year = year + 1
    else:
        leap_status = "Non Leap Year"
        anniversary_year = year - 1
    
    new_anniversary_date = date_obj.replace(year=anniversary_year).strftime('%d/%m/%Y')
    
    print(f"Given Anniversary Year: {leap_status}. Anniversary Date: {new_anniversary_date}")

input_date = '04/09/2004'
anniversary_date(input_date)
