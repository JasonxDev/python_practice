from datetime import date
from dateutil.relativedelta import relativedelta

# Take object for today's date and fast forward 2 months using dateutil library
today = date.today()  # Date object for 2023-12-27
yesterday = today + relativedelta(days=20)  # Date object for 2023-12-26
print(today)
# Now convert the date object to a string
dateString = yesterday.strftime("%Y-%m-%d")  # 2023-12-26
print(yesterday)

diff = abs(today - yesterday)
print(diff)