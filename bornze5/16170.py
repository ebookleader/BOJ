import datetime
utc0 = datetime.datetime.now() + datetime.timedelta(hours=9)
print(utc0.strftime("%Y"))
print(utc0.strftime("%m"))
print(utc0.strftime("%d"))
