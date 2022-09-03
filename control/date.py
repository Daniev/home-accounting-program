"""
date
-------
-----
"""

from datetime import date

MONTH_STRING = ["jan", "feb", "mar", "apr", "may",
                "jun", "jul", "aug", "sep", "okt", "nov",
                "des"]


def getCurrentMonth():
    """returns month number"""
    currentDate = date.today()
    return currentDate.month


def getMonthText(monthNumber):
    """
    Args:
        monthNumber (int): number of month 1-12

    Returns:
        string: month as string, ex: jan
    """
    months = MONTH_STRING
    return months[monthNumber - 1]
