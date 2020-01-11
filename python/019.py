import datetime
print(datetime.date(1990, 1, 1).weekday())
week_list = [0] * 7
for year in range(1901, 2000 + 1):
    for month in range(1, 12 + 1):
        weekday = datetime.date(year, month, 1).weekday()
        week_list[weekday] += 1
print(week_list)
