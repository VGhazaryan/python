import re
import datetime

file = open('text.txt')
allDates = []

def checkDate(date):
    isDate = True
    day, month, year = date.split('/')
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isDate = False
    return isDate

for i in file:
    dates = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", i)
    print(dates)
    for d in dates:
        if checkDate(d):
            allDates.append(d)
print(allDates)