import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay


a= pd.read_csv("C:/Users/pkpre/Downloads/premk.csv")

print(a)

weekdays = "Sat Sun Mon Tue Wed"


bday = CustomBusinessDay(holidays=['2022-08-10'],weekmask=weekdays)

b = pd.date_range(start="08-01-2022", end="08-15-2022", freq=bday)

print(b)
