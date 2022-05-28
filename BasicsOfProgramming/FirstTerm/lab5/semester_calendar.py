import calendar
def semester_calendar(output_type, year, first_month, last_month):
    """
    (str, int, int, int) -> str
    Returns the calendar of exact year which starts with first_month
    and ends with last_month
    >>> print(semester_calendar("txt", 2021, 10, 10))
        October 2021
    Mo Tu We Th Fr Sa Su
                 1  2  3
     4  5  6  7  8  9 10
    11 12 13 14 15 16 17
    18 19 20 21 22 23 24
    25 26 27 28 29 30 31
    <BLANKLINE>
    <BLANKLINE>    """
    res = ""
    if output_type == "txt":
        calen = calendar.TextCalendar(calendar.MONDAY)
        for i in range(first_month, last_month+1):
            onemonth=calen.formatmonth(year, i)
            res += onemonth+"\n"
        return res
    elif output_type == "html":
        calen = calendar.HTMLCalendar(calendar.MONDAY)
        for i in range(first_month, last_month+1):
            onemonth=calen.formatmonth(year, i, withyear=True)
            res += onemonth+"\n"
        return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()