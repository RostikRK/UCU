"""
high level support for doing this and that.
"""

def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]
    >>> weekday_name(3)
    'thu'
    """
    res =""
    if number == 0:
        res = "mon"
    elif number == 1:
        res = 'tue'
    elif number == 2:
        res = 'wed'
    elif number == 3:
        res = 'thu'
    elif number == 4:
        res = 'fri'
    elif number == 5:
        res = 'sat'
    elif number == 6:
        res = 'sun'
    else:
        res = None
    return res

	
def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message
    
    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    import calendar
    date_list = date.split(".")
    resul = calendar.weekday(int(date_list[2]), int(date_list[1]), int(date_list[0]))
    return resul

def calendar(month: int, year: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    import calendar
    res = ""
    calen = calendar.TextCalendar(calendar.MONDAY)
    monthh=calen.formatmonth(year, month, w=3)
    cal = monthh.lower()
    cal = cal[20:]
    lines = cal.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    for line in non_empty_lines:
        if line != non_empty_lines[-1]:
            res += line + "\n"
        elif line == non_empty_lines[-1]:
            res += line
    return res


def transform_calendar(calendar: str) -> str:
    """Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    None
    >>> print(transform_calendar(calendar(8 , 2015)))
    None
    """
    pass


if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (calendar(month, year))
    except ValueError as err:
        print(err)
