import re
import datetime

file = open('text.txt')
allDates = []
for i in file:
    print(file)
    dates = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", i)
    print(dates)
    for d in dates:
        isDate = True
        day, month, year = d.split('/')
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isDate = False
        if isDate:
            allDates.append(d)
print(allDates)