from datetime import datetime, timedelta, timezone

naïve_date = datetime(2023, 12, 21)
offset = timezone(timedelta(hours=-5))
x = naïve_date.replace(tzinfo=offset)  # 2023-12-21 00:00:00-05:00
y = x.strftime("%Y-%m-%dT%H:%M:%SZ")

print(x)
print(y)
