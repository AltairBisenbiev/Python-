import datetime as datetime 
day = datetime.datetime.today() - datetime.timedelta(days=5)
print(day.strftime("%D"))