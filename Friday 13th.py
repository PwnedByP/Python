'''
Find the next friday the 13th.

Write a function named friday_the_13th, which takes no parameter, and just returns the date of the next friday the 13th.

If today is a friday the 13th, return it, not the next one.

Return the date as a string of the following format: YYYY-MM-DD.

https://genepy.org/exercises/friday-the-13th
'''

from datetime import date


def friday_the_13th():
    today = date.today()
    month = today.month
    year = today.year
    if today.weekday() == 4 and today.day == 13:
        result = date(year, month, 13)
    elif today.day < 13:
        if date(year,month, 13).weekday() == 4:
            result = date(year,month,13)
        else:
            month += 1
            while date(year, month, 13).weekday() != 4:
                month += 1
                if month > 12:
                    month = 1
                    year += 1
            result = date(year, month, 13)
    else:
        month += 1
        while date(year, month, 13).weekday() != 4:
            month += 1
            if month > 12:
                month = 1
                year += 1
        result = date(year, month, 13)
    return result.strftime("%Y-%m-%d")


'''
Test
print(friday_the_13th())
'''
