# day = 13
# print("Сегодня пятница, {:10d}".format(day))
# print("Сегодня пятница, {:<10d}".format(day))
# print("Сегодня пятница, {:^10d}".format(day))


# day = 13
# month = 6
# hour = 15
# print("Сегодня пятница, {1:*>10n}.{0:*^5n}.{2:*<10n}".format(month, day, hour))
#
#
# day = "пятница"
# month = "июнь"
# day_time = "утро"
# print("Сегодня пятница, {1:*>10s}.{0:*^6s}.{2:*<10s}".format(month, day, day_time))

# print("Сегодня пятница, {day}.{month}.{day_time}".format(month="июнь", day="пятница", day_time="утро"))

day = 13
month = "июнь"
day_time = 15
print("Сегодня пятница, %d.%s.%d" % (day, month, day_time))
