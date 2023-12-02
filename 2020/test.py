from datetime import datetime, time


def getTicks (d1, d2):
    format_string = "%Y-%m-%d %H:%M"
    date1 = datetime.strptime(d1, format_string)
    date2 = datetime.strptime(d2, format_string)

    delta = int((date2 - date1).total_seconds()/60)
    return delta


#dateFrom = "1518-11-01 00:30"
#dateTo = "1518-11-01 00:55"

#print(getTicks (dateFrom,dateTo))


incr = 1

incr = incr * -1
print(incr)
