import calendar
import datetime as dt


def get_week():
    temp = dt.datetime.now()
    print(dt.datetime.now().date())
    print(temp.date().weekday())


get_week()
