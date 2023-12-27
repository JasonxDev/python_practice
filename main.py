from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()  # Date object for 2023-12-25
twoMonthsLater = today + relativedelta(months=2)  # Date object for 2024-02-25

# Now convert the date object to a string
dateString = twoMonthsLater.strftime("%m-%d-%Y")  # 02-25-2024
print(dateString)

