from datetime import datetime, date

# Define two date objects
date1 = datetime(2023, 12, 15)
date2 = datetime(2020, 12, 27)

# Calculate the day difference
day_difference = (date2 - date1)
absolute_day_difference = abs((date2 - date1).days)
# week_difference = (date2 - date1).weeks
# month_difference = (date2 - date1).months
# year_difference = (date2 - date1).years

print("day_difference", day_difference, absolute_day_difference)
# print("week_difference", week_difference)
# print("month_difference", month_difference)
# print("year_difference", year_difference)


f