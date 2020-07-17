import datetime
from threading import Timer


now = datetime.datetime.today()
soon = now.replace(day=now.day, hour=)
while now.minute != soon:
    print(datetime.date.weekday(now))