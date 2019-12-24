import re
from string_util_homework import string_util

file = open('text.txt')
allDates = []
checkDate = string_util.checkDate


for i in file:
    dates = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", i)
    print(dates)
    for d in dates:
        if checkDate(d):
            allDates.append(d)
print(allDates)