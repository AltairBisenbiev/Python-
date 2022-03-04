import datetime
day = datetime.datetime(2022,1,1)
day1 = datetime.datetime(2022,2,2)
a = day1-day
print(a.total_seconds())