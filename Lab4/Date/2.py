import datetime as datetime 
day = datetime.datetime.today() - datetime.timedelta(days=1)
print(day.strftime("%D"))
day = datetime.datetime.today()
print(day.strftime("%D"))
day = datetime.datetime.today() + datetime.timedelta(days=1)
print(day.strftime("%D"))