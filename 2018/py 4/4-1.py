import re


f = open("2018/py 4/4-test.txt", "r").readlines()

timetable = {}

## Create timetable
for line in f:
    line = line.strip()

    if "Guard" in line.strip():
        guardID = re.search('#..',line.strip()).group(0)[1:]
        schedule = [0 for i in range(60)]
        timetable.update({guardID: schedule})




for line in f:
    line = line.strip()

    day = re.search('-..-..',line).group(0)[-2:]
    hour = line[12:14]
    minute = line[15:17]

    #print(hour,":",minute)

    if "Guard" in line:
        guardID = re.search('#..',line).group(0)[1:]

    if "falls asleep" in line:
        startTime = 

    #timetable.update(guardID : )

    #print(line.strip())
